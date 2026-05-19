from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q
from user_app.models import CustomUser, Note

def admin_required(view_func):
    """Decorator to enforce that the logged-in user is a staff member or superuser."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Please log in with an administrator account.")
            return redirect('admin_app:login')
        if not (request.user.is_staff or request.user.is_superuser):
            messages.error(request, "Access denied. Administrator privileges are required.")
            return redirect('user_app:dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_login_view(request):
    """Custom login view for administrators (staff/superusers)."""
    if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
        return redirect('admin_app:dashboard')
        
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email', '').strip()
        password = request.POST.get('password', '')
        
        if not username_or_email or not password:
            messages.error(request, "Username/Email and Password are required.")
            return render(request, 'admin_app/login.html')
            
        username = username_or_email
        if '@' in username_or_email:
            try:
                user_obj = CustomUser.objects.get(email__iexact=username_or_email)
                username = user_obj.username
            except CustomUser.DoesNotExist:
                pass
                
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if not (user.is_staff or user.is_superuser):
                messages.error(request, "Access denied. You do not have administrator permissions.")
                return render(request, 'admin_app/login.html')
                
            if user.is_blocked:
                messages.error(request, "Access denied. This admin account has been blocked.")
                return render(request, 'admin_app/login.html')
                
            login(request, user)
            messages.success(request, f"Welcome to the Admin Command Center, {user.username}!")
            return redirect('admin_app:dashboard')
        else:
            messages.error(request, "Invalid administrator credentials.")
            
    return render(request, 'admin_app/login.html')


@admin_required
def admin_dashboard_view(request):
    """Custom admin panel showing registered user list, user stats, notes list, note stats, and feedback messages."""
    # Search filter
    search_query = request.GET.get('q', '').strip()
    
    users = CustomUser.objects.all().order_by('-date_joined')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) | 
            Q(email__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
        
    # Statistical aggregations for users
    stats = {
        'total': CustomUser.objects.count(),
        'verified': CustomUser.objects.filter(is_verified=True).count(),
        'blocked': CustomUser.objects.filter(is_blocked=True).count(),
        'pending': CustomUser.objects.filter(is_verified=False).count(),
    }
    
    # Fetch notes for administration
    notes = Note.objects.all().order_by('-created_at')
    
    # Statistical aggregations for notes
    note_stats = {
        'total': notes.count(),
        'pending': notes.filter(status='pending').count(),
        'approved': notes.filter(status='approved').count(),
        'rejected': notes.filter(status='rejected').count(),
    }

    # Fetch feedback messages
    from user_app.models import ContactMessage
    contact_messages = ContactMessage.objects.all().order_by('-created_at')
    
    context = {
        'users': users,
        'stats': stats,
        'notes': notes,
        'note_stats': note_stats,
        'contact_messages': contact_messages,
        'search_query': search_query
    }
    return render(request, 'admin_app/dashboard.html', context)


@admin_required
def block_user_view(request, user_id):
    """Blocks a user, preventing login access."""
    user_to_block = get_object_or_404(CustomUser, id=user_id)
    
    # Self check
    if user_to_block.id == request.user.id:
        messages.error(request, "Security protection: You cannot block your own admin account.")
        return redirect('admin_app:dashboard')
        
    user_to_block.is_blocked = True
    user_to_block.save()
    messages.success(request, f"User {user_to_block.username} has been successfully blocked.")
    return redirect('admin_app:dashboard')


@admin_required
def unblock_user_view(request, user_id):
    """Unblocks a user, restoring login access."""
    user_to_unblock = get_object_or_404(CustomUser, id=user_id)
    
    user_to_unblock.is_blocked = False
    user_to_unblock.save()
    messages.success(request, f"User {user_to_unblock.username} has been successfully unblocked.")
    return redirect('admin_app:dashboard')


@admin_required
def edit_user_view(request, user_id):
    """Renders a profile edit form and commits updates for a specific user."""
    user_to_edit = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        
        is_verified = request.POST.get('is_verified') == 'true'
        is_blocked = request.POST.get('is_blocked') == 'true'
        
        # Validations
        if not username or not email:
            messages.error(request, "Username and Email are required.")
            return render(request, 'admin_app/edit_user.html', {'target_user': user_to_edit})
            
        if CustomUser.objects.filter(username__iexact=username).exclude(id=user_to_edit.id).exists():
            messages.error(request, "Username is already taken by another user.")
            return render(request, 'admin_app/edit_user.html', {'target_user': user_to_edit})
            
        if CustomUser.objects.filter(email__iexact=email).exclude(id=user_to_edit.id).exists():
            messages.error(request, "Email is already taken by another user.")
            return render(request, 'admin_app/edit_user.html', {'target_user': user_to_edit})
            
        # Self protection for block/unblock and superuser controls
        if user_to_edit.id == request.user.id and is_blocked:
            messages.error(request, "Security protection: You cannot block your own admin account.")
            is_blocked = False
            
        try:
            user_to_edit.full_name = full_name
            user_to_edit.username = username
            user_to_edit.email = email
            user_to_edit.mobile = mobile
            user_to_edit.first_name = first_name
            user_to_edit.last_name = last_name
            user_to_edit.is_verified = is_verified
            user_to_edit.is_blocked = is_blocked
            user_to_edit.save()
            
            messages.success(request, f"User '{user_to_edit.username}' profile updated successfully.")
            return redirect('admin_app:dashboard')
            
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            
    return render(request, 'admin_app/edit_user.html', {'target_user': user_to_edit})


def send_note_status_html_email(note, is_approved):
    """Sends a beautifully designed HTML note moderation email with fallback to plain text."""
    from django.core.mail import send_mail
    from django.conf import settings

    if is_approved:
        subject = f"Your note submission has been APPROVED - FirstPortal"
        plain_message = (
            f"Hello {note.user.username},\n\n"
            f"We are pleased to inform you that your note titled '{note.title}' (Category: {note.category}) "
            f"has been APPROVED by the administrator.\n\n"
            f"You can now view it under your approved submissions on your dashboard.\n\n"
            f"Best regards,\n"
            f"The FirstPortal Admin Team"
        )
        header_color_1 = "#10b981"
        header_color_2 = "#059669"
        header_text_color = "#a7f3d0"
        badge_bg = "#ecfdf5"
        badge_text = "#047857"
        badge_border = "#a7f3d0"
        status_text = "Submission Approved"
        status_color = "#059669"
        status_label = "Approved"
    else:
        subject = f"Your note submission has been REJECTED - FirstPortal"
        plain_message = (
            f"Hello {note.user.username},\n\n"
            f"We regret to inform you that your note titled '{note.title}' (Category: {note.category}) "
            f"has been REJECTED by the administrator.\n\n"
            f"You can modify or review this submission from your dashboard.\n\n"
            f"Best regards,\n"
            f"The FirstPortal Admin Team"
        )
        header_color_1 = "#ef4444"
        header_color_2 = "#dc2626"
        header_text_color = "#fecaca"
        badge_bg = "#fff5f5"
        badge_text = "#b91c1c"
        badge_border = "#fecaca"
        status_text = "Submission Rejected"
        status_color = "#b91c1c"
        status_label = "Rejected"

    html_message = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Note Review Status - FirstPortal</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; padding: 40px 0;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 520px; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 24px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);">
                    <tr>
                        <td align="center" style="padding: 32px 40px 24px 40px; background: linear-gradient(135deg, {header_color_1} 0%, {header_color_2} 100%);">
                            <h2 style="margin: 0; font-size: 24px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">FirstPortal</h2>
                            <p style="margin: 4px 0 0 0; font-size: 13px; font-weight: 500; color: {header_text_color}; text-transform: uppercase; letter-spacing: 1.5px;">Document Moderation</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 40px 40px 32px 40px;">
                            <div style="margin-bottom: 24px; text-align: center;">
                                <span style="display: inline-block; padding: 6px 16px; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; border-radius: 9999px; background-color: {badge_bg}; color: {badge_text}; border: 1px solid {badge_border};">
                                    {status_text}
                                </span>
                            </div>
                            
                            <h3 style="margin: 0 0 16px 0; font-size: 18px; font-weight: 700; color: #0f172a; text-align: center;">Note Submission Update</h3>
                            
                            <p style="margin: 0 0 24px 0; font-size: 14px; line-height: 1.6; color: #475569; font-weight: 450;">
                                Hello <strong style="color: #0f172a;">{note.user.username}</strong>,<br><br>
                                The review process for your note submission has been completed by the portal administrator. Please find the decision and the details of your submission below:
                            </p>
                            
                            <div style="background-color: #f8fafc; border: 1px solid #f1f5f9; border-radius: 16px; padding: 20px; margin-bottom: 28px;">
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                    <tr>
                                        <td style="padding-bottom: 12px; border-bottom: 1px solid #f1f5f9; font-size: 12px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px;" width="35%">Note Title</td>
                                        <td style="padding-bottom: 12px; border-bottom: 1px solid #f1f5f9; font-size: 13px; font-weight: 700; color: #0f172a; text-align: right;">{note.title}</td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 12px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px;">Category</td>
                                        <td style="padding: 12px 0; border-bottom: 1px solid #f1f5f9; font-size: 13px; font-weight: 600; color: #4f46e5; text-align: right;">{note.category}</td>
                                    </tr>
                                    <tr>
                                        <td style="padding-top: 12px; font-size: 12px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px;">Review Status</td>
                                        <td style="padding-top: 12px; font-size: 13px; font-weight: 700; color: {status_color}; text-align: right; text-transform: uppercase; letter-spacing: 0.5px;">{status_label}</td>
                                    </tr>
                                </table>
                            </div>

                            <div style="text-align: center; margin-bottom: 12px;">
                                <a href="http://127.0.0.1:8000/login/" style="display: inline-block; padding: 14px 28px; background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); color: #ffffff; text-decoration: none; border-radius: 14px; font-size: 13px; font-weight: 700; letter-spacing: 0.5px; box-shadow: 0 4px 12px rgba(99, 102, 241, 0.25);">
                                    Access Your Dashboard
                                </a>
                            </div>
                            
                            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 32px 0 24px 0;">
                            
                            <p style="margin: 0; font-size: 12px; line-height: 1.5; color: #94a3b8; text-align: center; font-weight: 500;">
                                Thank you for contributing high-quality materials to the FirstPortal community.
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 24px 40px; background-color: #f8fafc; border-top: 1px solid #f1f5f9;">
                            <p style="margin: 0; font-size: 11px; font-weight: 600; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px;">FirstPortal System Notification</p>
                            <p style="margin: 4px 0 0 0; font-size: 11px; color: #cbd5e1; font-weight: 500;">&copy; 2026 FirstPortal. All rights reserved.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL or 'noreply@firstportal.local',
        recipient_list=[note.user.email],
        html_message=html_message,
        fail_silently=False
    )

@admin_required
def approve_note_view(request, note_id):
    """Approves a note and sends a confirmation email to the user."""
    note = get_object_or_404(Note, id=note_id)
    note.status = 'approved'
    note.save()
    
    try:
        send_note_status_html_email(note, is_approved=True)
        messages.success(request, f"Note '{note.title}' approved. A confirmation email has been sent to {note.user.email}.")
    except Exception as email_err:
        messages.warning(request, f"Note '{note.title}' approved, but the confirmation email could not be sent. Error: {str(email_err)}")
        
    return redirect('admin_app:dashboard')


@admin_required
def reject_note_view(request, note_id):
    """Rejects a note and sends a notification email to the user."""
    note = get_object_or_404(Note, id=note_id)
    note.status = 'rejected'
    note.save()
    
    try:
        send_note_status_html_email(note, is_approved=False)
        messages.success(request, f"Note '{note.title}' rejected. A notification email has been sent to {note.user.email}.")
    except Exception as email_err:
        messages.warning(request, f"Note '{note.title}' rejected, but the notification email could not be sent. Error: {str(email_err)}")
        
    return redirect('admin_app:dashboard')


@admin_required
def read_message_view(request, msg_id):
    """Marks a feedback message as read/unread."""
    from user_app.models import ContactMessage
    msg = get_object_or_404(ContactMessage, id=msg_id)
    msg.is_read = not msg.is_read  # Toggle
    msg.save()
    messages.success(request, f"Feedback message status updated successfully.")
    return redirect('admin_app:dashboard')


@admin_required
def delete_message_view(request, msg_id):
    """Deletes a feedback message from the database."""
    from user_app.models import ContactMessage
    msg = get_object_or_404(ContactMessage, id=msg_id)
    msg.delete()
    messages.success(request, "Feedback message successfully deleted.")
    return redirect('admin_app:dashboard')
