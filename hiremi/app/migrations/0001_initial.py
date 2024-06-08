# Generated by Django 5.0.6 on 2024-06-08 17:25

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorporateDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveIntegerField(help_text='Discount as a percentage (0-100).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('original_price', models.DecimalField(decimal_places=2, default=0.0, help_text='Original price before discount.', max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'verbose_name': 'Corporate Discount',
                'verbose_name_plural': 'Corporate Discounts',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveIntegerField(help_text='Discount as a percentage (0-100).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('original_price', models.DecimalField(decimal_places=2, default=0.0, help_text='Original price before discount.', max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
        migrations.CreateModel(
            name='FresherJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('code_required', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3)),
                ('code', models.PositiveIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('skills_required', models.CharField(max_length=255)),
                ('knowledge_stars', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5)])),
                ('who_can_apply', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('terms_and_conditions', models.TextField()),
                ('CTC', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Fresher Job',
                'verbose_name_plural': 'Fresher Jobs',
            },
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('code_required', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3)),
                ('code', models.PositiveIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('skills_required', models.CharField(max_length=255)),
                ('knowledge_stars', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5)])),
                ('who_can_apply', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('terms_and_conditions', models.TextField()),
                ('Stipend', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Internship',
                'verbose_name_plural': 'Internships',
            },
        ),
        migrations.CreateModel(
            name='MentorshipDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveIntegerField(help_text='Discount as a percentage (0-100).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('original_price', models.DecimalField(decimal_places=2, default=0.0, help_text='Original price before discount.', max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'verbose_name': 'Mentorship Discount',
                'verbose_name_plural': 'Mentorship Discounts',
            },
        ),
        migrations.CreateModel(
            name='OrderStatusResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(max_length=50)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('txn_id', models.CharField(blank=True, max_length=100, null=True)),
                ('result_msg', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Amount in currency.', max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('txn_token', models.CharField(max_length=100)),
                ('order_id', models.CharField(help_text='Unique identifier for the transaction.', max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Not Enroll', 'Not Enroll'), ('Enroll Pending', 'Enroll Pending'), ('Enrolled', 'Enrolled')], default='Not Enroll', max_length=15)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('unique', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('full_name', models.CharField(max_length=300)),
                ('father_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('whatsapp_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('college_state', models.CharField(max_length=100)),
                ('birth_place', models.CharField(max_length=100, null=True)),
                ('college_name', models.CharField(max_length=300)),
                ('branch_name', models.CharField(max_length=200)),
                ('degree_name', models.CharField(default='', max_length=200)),
                ('passing_year', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(8)])),
                ('verified', models.BooleanField(default=False)),
                ('otp', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)])),
            ],
            options={
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registers',
            },
        ),
        migrations.CreateModel(
            name='Mentorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Not Enroll', 'Not Enroll'), ('Enroll Pending', 'Enroll Pending'), ('Enrolled', 'Enrolled')], default='Not Enroll', max_length=15)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('candidate_status', models.CharField(choices=[('Applied', 'Applied'), ('Select', 'Select'), ('Pending', 'Pending'), ('Reject', 'Reject'), ('EXPIRE', 'EXPIRE'), ('DirectSelect', 'DirectSelect')], default='Applied', max_length=12)),
                ('applied', models.BooleanField(default=False)),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='app.register')),
            ],
            options={
                'verbose_name': 'Mentorship',
                'verbose_name_plural': 'Mentorships',
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_status', models.CharField(choices=[('Pending', 'Pending'), ('Select', 'Select'), ('Reject', 'Reject')], default='Pending', max_length=10)),
                ('fresherjob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='app.fresherjob')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='app.register')),
            ],
            options={
                'verbose_name': 'Job Application',
                'verbose_name_plural': 'Job Applications',
            },
        ),
        migrations.CreateModel(
            name='InternshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_status', models.CharField(choices=[('Pending', 'Pending'), ('Select', 'Select'), ('Reject', 'Reject')], default='Pending', max_length=10)),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='app.internship')),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='app.register')),
            ],
            options={
                'verbose_name': 'Internship Application',
                'verbose_name_plural': 'Internship Applications',
            },
        ),
        migrations.CreateModel(
            name='CorporateTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Not Enroll', 'Not Enroll'), ('Enroll Pending', 'Enroll Pending'), ('Enrolled', 'Enrolled')], default='Not Enroll', max_length=15)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('candidate_status', models.CharField(choices=[('Applied', 'Applied'), ('Select', 'Select'), ('Pending', 'Pending'), ('Reject', 'Reject'), ('EXPIRE', 'EXPIRE'), ('DirectSelect', 'DirectSelect')], default='Applied', max_length=12)),
                ('applied', models.BooleanField(default=False)),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='app.register')),
            ],
            options={
                'verbose_name': 'Corporate Training',
                'verbose_name_plural': 'Corporate Trainings',
            },
        ),
        migrations.CreateModel(
            name='ScoreCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=255)),
                ('scores', models.JSONField()),
                ('average_score_stars', models.PositiveIntegerField(default=0)),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scorecards', to='app.register')),
            ],
            options={
                'verbose_name': 'ScoreCard',
                'verbose_name_plural': 'ScoreCards',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('uid', models.CharField(max_length=50, unique=True)),
                ('issue', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='app.register')),
            ],
        ),
        migrations.CreateModel(
            name='VerificationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Not Enroll', 'Not Enroll'), ('Enroll Pending', 'Enroll Pending'), ('Enrolled', 'Enrolled')], default='Not Enroll', max_length=15)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('uid', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('college_id_number', models.CharField(default='', max_length=20, unique=True)),
                ('communication_skills', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
                ('Describe_experience', models.TextField(max_length=500)),
                ('skills', models.CharField(blank=True, max_length=100, null=True)),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verification_details', to='app.register')),
            ],
            options={
                'verbose_name': 'Verification Detail',
                'verbose_name_plural': 'Verification Details',
            },
        ),
    ]
