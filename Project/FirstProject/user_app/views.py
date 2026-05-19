from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import CustomUser, Note

def send_otp_html_email(username, email, otp):
    """Sends a beautifully styled HTML OTP email with fallback to plain text."""
    subject = "Verify Your Account - FirstPortal"
    
    plain_message = (
        f"Hello {username},\n\n"
        f"Thank you for registering at FirstPortal!\n\n"
        f"Your 6-digit OTP code is: {otp}\n"
        f"This code will expire in 10 minutes.\n\n"
        f"If you did not request this code, please ignore this email."
    )
    
    html_message = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verify Your Account - FirstPortal</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; padding: 40px 0;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 520px; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 24px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);">
                    <tr>
                        <td align="center" style="padding: 32px 40px 24px 40px; background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);">
                            <h2 style="margin: 0; font-size: 24px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">FirstPortal</h2>
                            <p style="margin: 4px 0 0 0; font-size: 13px; font-weight: 500; color: #c7d2fe; text-transform: uppercase; letter-spacing: 1.5px;">Secure Verification</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 40px 40px 32px 40px;">
                            <h3 style="margin: 0 0 16px 0; font-size: 18px; font-weight: 700; color: #0f172a;">Account Verification Required</h3>
                            <p style="margin: 0 0 24px 0; font-size: 14px; line-height: 1.6; color: #475569; font-weight: 450;">
                                Hello <strong style="color: #0f172a;">{username}</strong>,<br><br>
                                Thank you for joining FirstPortal! Please use the following 6-digit verification code to complete your registration and secure your profile.
                            </p>
                            
                            <div style="background-color: #f1f5f9; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; text-align: center; margin-bottom: 24px;">
                                <span style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 2px; display: block; margin-bottom: 8px;">Your OTP Verification Code</span>
                                <span style="font-size: 36px; font-weight: 800; color: #4f46e5; letter-spacing: 6px; font-family: Menlo, Monaco, Consolas, monospace; display: block;">{otp}</span>
                            </div>

                            <p style="margin: 0 0 24px 0; font-size: 13px; line-height: 1.5; color: #92400e; font-weight: 500; text-align: center; background-color: #fef3c7; border: 1px solid #fde68a; border-radius: 12px; padding: 12px 16px;">
                                <strong>Safety Notice:</strong> This code is valid for exactly <strong>10 minutes</strong>. Never share this code with anyone, including members of our support team.
                            </p>
                            
                            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 32px 0 24px 0;">
                            
                            <p style="margin: 0; font-size: 12px; line-height: 1.5; color: #94a3b8; text-align: center; font-weight: 500;">
                                If you did not request this code, you can safely ignore this email.
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
        recipient_list=[email],
        html_message=html_message,
        fail_silently=False
    )

def register_view(request):
    """Handles user registration and OTP dispatch."""
    if request.user.is_authenticated:
        return redirect('user_app:dashboard')
        
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        # Simple validations
        if not full_name or not username or not email or not mobile or not password:
            messages.error(request, "All fields are required.")
            return render(request, 'user_app/register.html')
            
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'user_app/register.html')
            
        if CustomUser.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'user_app/register.html')
            
        if CustomUser.objects.filter(email__iexact=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'user_app/register.html')
            
        try:
            # Create user (inactive or active but unverified)
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                full_name=full_name,
                mobile=mobile
            )
            # Generate and save OTP
            otp = user.generate_otp()
            
            # Send Beautiful HTML Email
            send_otp_html_email(user.username, email, otp)
            
            # Store email in session to verify OTP on next step
            request.session['verification_email'] = email
            messages.success(request, "Registration successful! We have sent a 6-digit OTP code to your email.")
            return redirect('user_app:verify_otp')
            
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'user_app/register.html')
            
    return render(request, 'user_app/register.html')


def verify_otp_view(request):
    """Verifies the OTP sent to user's email."""
    email = request.session.get('verification_email')
    
    if not email:
        messages.error(request, "No verification session found. Please register or log in.")
        return redirect('user_app:login')
        
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('user_app:register')
        
    if request.method == 'POST':
        otp_code = request.POST.get('otp_code', '').strip()
        
        if not otp_code:
            messages.error(request, "Please enter the 6-digit OTP code.")
            return render(request, 'user_app/verify_otp.html', {'email': email})
            
        # Verify the OTP
        if user.verify_otp(otp_code):
            # Clean session
            del request.session['verification_email']
            
            # Directly log in the user
            login(request, user)
            messages.success(request, f"Welcome {user.username}! Your email has been verified successfully.")
            return redirect('user_app:dashboard')
        else:
            messages.error(request, "Invalid or expired OTP. Please try again.")
            
    return render(request, 'user_app/verify_otp.html', {'email': email})


def login_view(request):
    """Handles standard user login, block checks, and redirect to OTP validation if unverified."""
    if request.user.is_authenticated:
        return redirect('user_app:dashboard')
        
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email', '').strip()
        password = request.POST.get('password', '')
        
        if not username_or_email or not password:
            messages.error(request, "Username/Email and Password are required.")
            return render(request, 'user_app/login.html')
            
        # Resolve username if email is provided
        username = username_or_email
        if '@' in username_or_email:
            try:
                user_obj = CustomUser.objects.get(email__iexact=username_or_email)
                username = user_obj.username
            except CustomUser.DoesNotExist:
                # Let authenticate() handle failure
                pass
                
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user is blocked
            if user.is_blocked:
                messages.error(request, "Access denied. Your account has been blocked by the administrator.")
                return render(request, 'user_app/login.html')
                
            # Check if user is verified
            if not user.is_verified:
                otp = user.generate_otp()
                # Resend OTP in HTML
                send_otp_html_email(user.username, user.email, otp)
                
                request.session['verification_email'] = user.email
                messages.warning(request, "Your email is not verified yet. We have sent a new OTP to your email.")
                return redirect('user_app:verify_otp')
                
            # Perform login
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('user_app:dashboard')
        else:
            messages.error(request, "Invalid username/email or password.")
            
    return render(request, 'user_app/login.html')


def logout_view(request):
    """Logs out standard user."""
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('user_app:login')


@login_required
def dashboard_view(request):
    """Renders standard user dashboard with metrics and user's notes."""
    # Extra security check for blocks or unverified states
    if request.user.is_blocked:
        logout(request)
        messages.error(request, "Your account has been blocked by the administrator.")
        return redirect('user_app:login')
        
    if not request.user.is_verified:
        logout(request)
        messages.error(request, "Please verify your email first.")
        return redirect('user_app:login')
        
    # Get all notes for the logged in user
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    
    # Calculate stats
    stats = {
        'total': notes.count(),
        'pending': notes.filter(status='pending').count(),
        'approved': notes.filter(status='approved').count(),
        'rejected': notes.filter(status='rejected').count(),
    }
    
    context = {
        'notes': notes,
        'stats': stats,
    }
    return render(request, 'user_app/dashboard.html', context)


@login_required
def submit_note_view(request):
    """Allows standard users to submit a new note. Defaults to pending status."""
    if request.user.is_blocked:
        logout(request)
        messages.error(request, "Your account has been blocked.")
        return redirect('user_app:login')

    if not request.user.is_verified:
        logout(request)
        messages.error(request, "Please verify your email first.")
        return redirect('user_app:login')

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        category = request.POST.get('category', '').strip()
        file = request.FILES.get('file')

        if not title or not description or not category:
            messages.error(request, "Title, Description, and Category are required.")
            return render(request, 'user_app/submit_note.html')

        try:
            note = Note.objects.create(
                user=request.user,
                title=title,
                description=description,
                category=category,
                file=file,
                status='pending'  # Explicitly default to pending
            )
            messages.success(request, f"Note '{note.title}' submitted successfully! It is now pending administrator approval.")
            return redirect('user_app:dashboard')
        except Exception as e:
            messages.error(request, f"An error occurred while saving the note: {str(e)}")
            return render(request, 'user_app/submit_note.html')

    return render(request, 'user_app/submit_note.html')


@login_required
def update_note_view(request, note_id):
    """Allows standard users to update their notes. Resets status back to pending."""
    if request.user.is_blocked:
        logout(request)
        messages.error(request, "Your account has been blocked.")
        return redirect('user_app:login')

    if not request.user.is_verified:
        logout(request)
        messages.error(request, "Please verify your email first.")
        return redirect('user_app:login')

    from django.shortcuts import get_object_or_404
    note = get_object_or_404(Note, id=note_id, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        category = request.POST.get('category', '').strip()
        file = request.FILES.get('file')
        clear_file = request.POST.get('clear_file') == 'true'

        if not title or not description or not category:
            messages.error(request, "Title, Description, and Category are required.")
            return render(request, 'user_app/edit_note.html', {'note': note})

        try:
            note.title = title
            note.description = description
            note.category = category
            
            if file:
                note.file = file
            elif clear_file:
                note.file = None
                
            note.status = 'pending'  # Reset back to pending on update!
            note.save()
            messages.success(request, f"Note '{note.title}' updated successfully! It has been returned to pending status for administrator review.")
            return redirect('user_app:dashboard')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'user_app/edit_note.html', {'note': note})

    return render(request, 'user_app/edit_note.html', {'note': note})


def send_forgot_password_html_email(username, email, otp):
    """Sends a beautifully styled HTML password recovery OTP email."""
    subject = "Password Reset Request - FirstPortal"
    
    plain_message = (
        f"Hello {username},\n\n"
        f"We received a request to reset your FirstPortal password.\n\n"
        f"Your 6-digit OTP code is: {otp}\n"
        f"This code will expire in 10 minutes.\n\n"
        f"If you did not request a password reset, please ignore this email."
    )
    
    html_message = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Your Password - FirstPortal</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; padding: 40px 0;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 520px; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 24px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);">
                    <tr>
                        <td align="center" style="padding: 32px 40px 24px 40px; background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);">
                            <h2 style="margin: 0; font-size: 24px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">FirstPortal</h2>
                            <p style="margin: 4px 0 0 0; font-size: 13px; font-weight: 500; color: #c7d2fe; text-transform: uppercase; letter-spacing: 1.5px;">Password Recovery</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 40px 40px 32px 40px;">
                            <h3 style="margin: 0 0 16px 0; font-size: 18px; font-weight: 700; color: #0f172a;">Password Reset OTP Code</h3>
                            <p style="margin: 0 0 24px 0; font-size: 14px; line-height: 1.6; color: #475569; font-weight: 450;">
                                Hello <strong style="color: #0f172a;">{username}</strong>,<br><br>
                                We received a request to reset your account password. Please use the following 6-digit verification code to complete your password recovery:
                            </p>
                            
                            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; text-align: center; margin-bottom: 24px;">
                                <span style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 2px; display: block; margin-bottom: 8px;">Your Reset Code</span>
                                <span style="font-size: 36px; font-weight: 800; color: #4f46e5; letter-spacing: 6px; font-family: Menlo, Monaco, Consolas, monospace; display: block;">{otp}</span>
                            </div>

                            <p style="margin: 0 0 24px 0; font-size: 13px; line-height: 1.5; color: #92400e; font-weight: 500; text-align: center; background-color: #fef3c7; border: 1px solid #fde68a; border-radius: 12px; padding: 12px 16px;">
                                <strong>Important:</strong> This reset code is only valid for <strong>10 minutes</strong>. If you did not make this request, you can safely ignore this email; your credentials remain secure.
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
        recipient_list=[email],
        html_message=html_message,
        fail_silently=False
    )


def send_contact_thankyou_html_email(name, email, subject_text):
    """Sends a beautifully styled HTML contact form acknowledgment."""
    subject = "We have received your message - FirstPortal"
    
    plain_message = (
        f"Hello {name},\n\n"
        f"Thank you for contacting FirstPortal!\n\n"
        f"This is an automated confirmation to let you know that we have received your inquiry: "
        f"'{subject_text}'. Our team is currently reviewing your submission and will get back to you shortly.\n\n"
        f"Best regards,\n"
        f"The FirstPortal Admin Team"
    )
    
    html_message = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You - FirstPortal</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafc; padding: 40px 0;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 520px; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 24px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);">
                    <tr>
                        <td align="center" style="padding: 32px 40px 24px 40px; background: linear-gradient(135deg, #10b981 0%, #059669 100%);">
                            <h2 style="margin: 0; font-size: 24px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">FirstPortal</h2>
                            <p style="margin: 4px 0 0 0; font-size: 13px; font-weight: 500; color: #a7f3d0; text-transform: uppercase; letter-spacing: 1.5px;">Message Acknowledged</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 40px 40px 32px 40px;">
                            <h3 style="margin: 0 0 16px 0; font-size: 18px; font-weight: 700; color: #0f172a;">Thank You For Reaching Out!</h3>
                            <p style="margin: 0 0 24px 0; font-size: 14px; line-height: 1.6; color: #475569; font-weight: 450;">
                                Hello <strong style="color: #0f172a;">{name}</strong>,<br><br>
                                We have successfully received your contact message titled <strong style="color: #4f46e5;">"{subject_text}"</strong>.
                            </p>
                            
                            <div style="background-color: #f0fdf4; border: 1px solid #d1fae5; border-radius: 16px; padding: 20px; margin-bottom: 24px; text-align: center; color: #065f46; font-size: 13px; font-weight: 500; line-height: 1.5;">
                                Our support and administrator team is currently reviewing your inquiry. We typically reply to all feedback within <strong>24 business hours</strong>.
                            </div>

                            <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 32px 0 24px 0;">
                            
                            <p style="margin: 0; font-size: 12px; line-height: 1.5; color: #94a3b8; text-align: center; font-weight: 500;">
                                This is an automated email confirmation. Please do not reply directly to this address.
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding: 24px 40px; background-color: #f8fafc; border-top: 1px solid #f1f5f9;">
                            <p style="margin: 0; font-size: 11px; font-weight: 600; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px;">FirstPortal Support Notification</p>
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
        from_email=settings.DEFAULT_FROM_EMAIL or 'support@firstportal.local',
        recipient_list=[email],
        html_message=html_message,
        fail_silently=False
    )


def forgot_password_view(request):
    """Initiates user password reset with an email OTP verification."""
    if request.user.is_authenticated:
        return redirect('user_app:dashboard')
        
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if not email:
            messages.error(request, "Please enter your registered email address.")
            return render(request, 'user_app/forgot_password.html')
            
        try:
            user = CustomUser.objects.get(email__iexact=email)
            # Generate recovery OTP
            otp = user.generate_otp()
            # Send Beautiful HTML recovery OTP email
            send_forgot_password_html_email(user.username, user.email, otp)
            
            request.session['reset_email'] = user.email
            messages.success(request, "We have sent a 6-digit password recovery OTP code to your email.")
            return redirect('user_app:reset_password')
        except CustomUser.DoesNotExist:
            messages.error(request, "No account was found registered with this email address.")
            return render(request, 'user_app/forgot_password.html')
            
    return render(request, 'user_app/forgot_password.html')


def reset_password_view(request):
    """Verifies recovery OTP and resets the password securely."""
    if request.user.is_authenticated:
        return redirect('user_app:dashboard')
        
    email = request.session.get('reset_email')
    if not email:
        messages.error(request, "No recovery session found. Please enter your email to start over.")
        return redirect('user_app:forgot_password')
        
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('user_app:forgot_password')
        
    if request.method == 'POST':
        otp_code = request.POST.get('otp_code', '').strip()
        new_password = request.POST.get('new_password', '')
        confirm_new_password = request.POST.get('confirm_new_password', '')
        
        if not otp_code or not new_password or not confirm_new_password:
            messages.error(request, "All fields are required.")
            return render(request, 'user_app/reset_password.html', {'email': email})
            
        if new_password != confirm_new_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'user_app/reset_password.html', {'email': email})
            
        # Verify recovery OTP
        if user.verify_otp(otp_code):
            # Update password securely
            user.set_password(new_password)
            user.save()
            
            # Clean up recovery session
            del request.session['reset_email']
            messages.success(request, f"Password reset successful! You can now log in, {user.username}.")
            return redirect('user_app:login')
        else:
            messages.error(request, "Invalid or expired recovery OTP. Please check your inbox and try again.")
            
    return render(request, 'user_app/reset_password.html', {'email': email})


def about_view(request):
    """Displays the gorgeous light-themed About Us page with testimonials and videos."""
    return render(request, 'user_app/about.html')


def contact_view(request):
    """Displays contact page with interactive map and processes contact messages."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        if not name or not email or not subject or not message:
            messages.error(request, "All contact fields are required.")
            return render(request, 'user_app/contact.html')
            
        try:
            # Save feedback record in the database
            from .models import ContactMessage
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Send thank you email
            send_contact_thankyou_html_email(name, email, subject)
            
            messages.success(request, "Thank you! Your message has been sent successfully. We've sent an acknowledgment email to you.")
            return redirect('user_app:contact')
        except Exception as err:
            messages.error(request, f"An error occurred while sending your message: {str(err)}")
            return render(request, 'user_app/contact.html')
            
    return render(request, 'user_app/contact.html')
