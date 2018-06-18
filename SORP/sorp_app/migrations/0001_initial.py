# Generated by Django 2.0.6 on 2018-06-17 14:03

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('id', models.IntegerField(unique=True)),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('id', models.IntegerField(unique=True)),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('document', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sgpi', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=5)),
                ('cgpi', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='StudentBasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name_eng', models.CharField(max_length=60)),
                ('student_name_hindi', models.CharField(max_length=60, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'other')], max_length=10)),
                ('date_of_birth', models.DateField(max_length=8)),
                ('religion', models.CharField(max_length=30)),
                ('student_contact', models.IntegerField(null=True)),
                ('aadhar_no', models.IntegerField(null=True, unique='True')),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Urban', 'Urban')], max_length=10)),
                ('bonafide_country', models.CharField(max_length=30)),
                ('bonafide_state', models.CharField(max_length=30)),
                ('correspondence_add', models.CharField(max_length=1000)),
                ('permanent_add', models.CharField(max_length=1000)),
                ('nearest_railway_st', models.CharField(max_length=70)),
                ('year_of_admission', models.IntegerField()),
                ('jee_roll_no', models.BigIntegerField()),
                ('jee_score', models.IntegerField()),
                ('jee_AI_rank', models.IntegerField()),
                ('jee_category_rank', models.IntegerField()),
                ('admission_category', models.CharField(max_length=10)),
                ('intermediate_pass_country', models.CharField(max_length=30)),
                ('intermediate_pass_state', models.CharField(max_length=30)),
                ('intermediate_percentage', models.DecimalField(decimal_places=3, max_digits=5)),
                ('intermediate_pass_year', models.CharField(max_length=4)),
                ('intermediate_school_type', models.CharField(choices=[('Government', 'Government School'), ('Private', 'Private School')], max_length=20)),
                ('intermediate_school_area', models.CharField(choices=[('Rural', 'Rural'), ('Urban', 'Urban')], max_length=10)),
                ('intermediate_school_name', models.CharField(max_length=60)),
                ('hosteler', models.BooleanField()),
                ('hostel_name', models.CharField(choices=[('KBH', 'Kailash Boys Hostel'), ('Satpura', 'Satpuara Hostel'), ('Himadri', 'Himadri Boys Hostel'), ('Himgiri', 'Himgiri Boys Hostel'), ('NBH', 'Neelkanth Boys Hostel'), ('MMH', 'Manimahesh Boys Hostel'), ('VBH', 'Vindhyanchal Boys Hostel'), ('DBH', 'Dauladhar Boys Hostel'), ('AGH', 'Ambika Girls Hostel'), ('PGH', 'Parvati Girls Hostel')], max_length=50)),
                ('entry_no', models.IntegerField(default=None)),
                ('reg_no', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('father_name', models.CharField(max_length=60)),
                ('father_contact', models.IntegerField()),
                ('father_email', models.EmailField(max_length=254)),
                ('mother_name', models.CharField(max_length=60)),
                ('mother_contact', models.IntegerField()),
                ('mother_email', models.EmailField(max_length=254)),
                ('guardian_name', models.CharField(max_length=60)),
                ('guardian_contact', models.IntegerField()),
                ('guardian_email', models.EmailField(max_length=254)),
                ('family_income', models.IntegerField(default=0)),
                ('fee_waiver_claim', models.CharField(max_length=60)),
                ('intermediate_school_board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sorp_app.Board')),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sorp_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='StudentFirstFeeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_josaa_amount', models.IntegerField()),
                ('fee_josaa_date', models.DateField(default=None)),
                ('fee_NITH_amount', models.IntegerField()),
                ('fee_nith_date', models.DateField(default=None)),
                ('fee_NIT_receipt_no', models.CharField(max_length=25)),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sorp_app.StudentBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMedicalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('identification_mark', models.CharField(max_length=40)),
                ('major_illness', models.CharField(max_length=40)),
                ('blood_group', models.CharField(max_length=5)),
                ('vision', models.CharField(max_length=3)),
                ('height_in_cm', models.IntegerField()),
                ('past_mental_illness', models.CharField(max_length=30)),
                ('clour_blindness', models.CharField(max_length=10)),
                ('any_other_defect', models.CharField(max_length=30)),
                ('student_id', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='sorp_app.StudentBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_code', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UGBranch',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=400)),
                ('code', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='UGClass',
            fields=[
                ('id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='subjects',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sorp_app.UGBranch'),
        ),
        migrations.AddField(
            model_name='subjects',
            name='classname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sorp_app.UGClass'),
        ),
        migrations.AddField(
            model_name='studentbasicinfo',
            name='ug_branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sorp_app.UGBranch'),
        ),
        migrations.AddField(
            model_name='studentbasicinfo',
            name='ug_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sorp_app.UGClass'),
        ),
        migrations.AddField(
            model_name='studentbasicinfo',
            name='user_id',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='result',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sorp_app.StudentBasicInfo'),
        ),
        migrations.AddField(
            model_name='documents',
            name='stud_doc',
            field=models.ManyToManyField(through='sorp_app.DocumentInfo', to='sorp_app.StudentBasicInfo'),
        ),
        migrations.AddField(
            model_name='documentinfo',
            name='doc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sorp_app.Documents'),
        ),
        migrations.AddField(
            model_name='documentinfo',
            name='stud_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sorp_app.StudentBasicInfo'),
        ),
    ]