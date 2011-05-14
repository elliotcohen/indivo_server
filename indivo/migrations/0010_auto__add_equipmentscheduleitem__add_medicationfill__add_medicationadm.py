# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EquipmentScheduleItem'
        db.create_table('indivo_equipmentscheduleitem', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('name_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('name_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('scheduled_by', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_scheduled', self.gf('django.db.models.fields.DateField')(null=True)),
            ('date_start', self.gf('django.db.models.fields.DateField')(null=True)),
            ('date_end', self.gf('django.db.models.fields.DateField')(null=True)),
            ('recurrencerule_frequency', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('recurrencerule_frequency_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('recurrencerule_frequency_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('recurrencerule_frequency_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('recurrencerule_interval', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('recurrencerule_interval_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('recurrencerule_interval_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('recurrencerule_interval_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('recurrencerule_dateuntil', self.gf('django.db.models.fields.DateField')(null=True)),
            ('recurrencerule_count', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('instructions', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('indivo', ['EquipmentScheduleItem'])

        # Adding model 'MedicationFill'
        db.create_table('indivo_medicationfill', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('name_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('name_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('filled_by', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('date_filled', self.gf('django.db.models.fields.DateField')(null=True)),
            ('amountfilled_unit', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('amountfilled_textvalue', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('amountfilled_value', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('amountfilled_unit_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('amountfilled_unit_value', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('amountfilled_unit_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('ndc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ndc_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('ndc_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('ndc_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('fill_sequence_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('lot_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('refills_remaining', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('instructions', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('indivo', ['MedicationFill'])

        # Adding model 'MedicationAdministration'
        db.create_table('indivo_medicationadministration', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('name_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('name_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('reported_by', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('date_reported', self.gf('django.db.models.fields.DateField')(null=True)),
            ('date_administered', self.gf('django.db.models.fields.DateField')(null=True)),
            ('amountadministered_unit', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('amountadministered_textvalue', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('amountadministered_value', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('amountadministered_unit_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('amountadministered_unit_value', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('amountadministered_unit_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('amountremaining_unit', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('amountremaining_textvalue', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('amountremaining_value', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('amountremaining_unit_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('amountremaining_unit_value', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('amountremaining_unit_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal('indivo', ['MedicationAdministration'])

        # Deleting field 'VideoMessage.datetime_sent'
        db.delete_column('indivo_videomessage', 'datetime_sent')

        # Deleting field 'VideoMessage.datetime_recorded'
        db.delete_column('indivo_videomessage', 'datetime_recorded')

        # Adding field 'VideoMessage.date_recorded'
        db.add_column('indivo_videomessage', 'date_recorded', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'VideoMessage.date_sent'
        db.add_column('indivo_videomessage', 'date_sent', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Deleting field 'AdherenceItem.datetime_reported'
        db.delete_column('indivo_adherenceitem', 'datetime_reported')

        # Adding field 'AdherenceItem.date_reported'
        db.add_column('indivo_adherenceitem', 'date_reported', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'AdherenceItem.recurrence_index'
        db.add_column('indivo_adherenceitem', 'recurrence_index', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Changing field 'MedicationOrder.refills'
        db.alter_column('indivo_medicationorder', 'refills', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'MedicationOrder.date_expires'
        db.alter_column('indivo_medicationorder', 'date_expires', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'MedicationOrder.substitution_permitted'
        db.alter_column('indivo_medicationorder', 'substitution_permitted', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'MedicationOrder.date_ordered'
        db.alter_column('indivo_medicationorder', 'date_ordered', self.gf('django.db.models.fields.DateField')(null=True))

        # Deleting field 'MedicationScheduleItem.datetime_scheduled'
        db.delete_column('indivo_medicationscheduleitem', 'datetime_scheduled')

        # Adding field 'MedicationScheduleItem.date_scheduled'
        db.add_column('indivo_medicationscheduleitem', 'date_scheduled', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.date_start'
        db.add_column('indivo_medicationscheduleitem', 'date_start', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.date_end'
        db.add_column('indivo_medicationscheduleitem', 'date_end', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_frequency'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_frequency', self.gf('django.db.models.fields.CharField')(default=None, max_length=200), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_frequency_type'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_frequency_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_frequency_value'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_frequency_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_frequency_abbrev'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_frequency_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_interval'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_interval', self.gf('django.db.models.fields.CharField')(default=None, max_length=200), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_interval_type'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_interval_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_interval_value'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_interval_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_interval_abbrev'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_interval_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_dateuntil'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_dateuntil', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'MedicationScheduleItem.recurrencerule_count'
        db.add_column('indivo_medicationscheduleitem', 'recurrencerule_count', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Deleting field 'Vitals.date_measured'
        db.delete_column('indivo_vitals', 'date_measured')

        # Deleting field 'Vitals.unit'
        db.delete_column('indivo_vitals', 'unit')

        # Deleting field 'Vitals.value'
        db.delete_column('indivo_vitals', 'value')

        # Deleting field 'Vitals.unit_abbrev'
        db.delete_column('indivo_vitals', 'unit_abbrev')

        # Deleting field 'Vitals.unit_type'
        db.delete_column('indivo_vitals', 'unit_type')

        # Deleting field 'Vitals.unit_value'
        db.delete_column('indivo_vitals', 'unit_value')

        # Adding field 'Vitals.measured_by'
        db.add_column('indivo_vitals', 'measured_by', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Vitals.date_measured_start'
        db.add_column('indivo_vitals', 'date_measured_start', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'Vitals.date_measured_end'
        db.add_column('indivo_vitals', 'date_measured_end', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'Vitals.result_unit'
        db.add_column('indivo_vitals', 'result_unit', self.gf('django.db.models.fields.CharField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Vitals.result_textvalue'
        db.add_column('indivo_vitals', 'result_textvalue', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Vitals.result_value'
        db.add_column('indivo_vitals', 'result_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Vitals.result_unit_type'
        db.add_column('indivo_vitals', 'result_unit_type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Vitals.result_unit_value'
        db.add_column('indivo_vitals', 'result_unit_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Vitals.result_unit_abbrev'
        db.add_column('indivo_vitals', 'result_unit_abbrev', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'Vitals.technique'
        db.add_column('indivo_vitals', 'technique', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'EquipmentScheduleItem'
        db.delete_table('indivo_equipmentscheduleitem')

        # Deleting model 'MedicationFill'
        db.delete_table('indivo_medicationfill')

        # Deleting model 'MedicationAdministration'
        db.delete_table('indivo_medicationadministration')

        # Adding field 'VideoMessage.datetime_sent'
        db.add_column('indivo_videomessage', 'datetime_sent', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'VideoMessage.datetime_recorded'
        db.add_column('indivo_videomessage', 'datetime_recorded', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Deleting field 'VideoMessage.date_recorded'
        db.delete_column('indivo_videomessage', 'date_recorded')

        # Deleting field 'VideoMessage.date_sent'
        db.delete_column('indivo_videomessage', 'date_sent')

        # Adding field 'AdherenceItem.datetime_reported'
        db.add_column('indivo_adherenceitem', 'datetime_reported', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Deleting field 'AdherenceItem.date_reported'
        db.delete_column('indivo_adherenceitem', 'date_reported')

        # Deleting field 'AdherenceItem.recurrence_index'
        db.delete_column('indivo_adherenceitem', 'recurrence_index')

        # Changing field 'MedicationOrder.refills'
        db.alter_column('indivo_medicationorder', 'refills', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'MedicationOrder.date_expires'
        db.alter_column('indivo_medicationorder', 'date_expires', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'MedicationOrder.substitution_permitted'
        db.alter_column('indivo_medicationorder', 'substitution_permitted', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'MedicationOrder.date_ordered'
        db.alter_column('indivo_medicationorder', 'date_ordered', self.gf('django.db.models.fields.DateField')(default=None))

        # Adding field 'MedicationScheduleItem.datetime_scheduled'
        db.add_column('indivo_medicationscheduleitem', 'datetime_scheduled', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Deleting field 'MedicationScheduleItem.date_scheduled'
        db.delete_column('indivo_medicationscheduleitem', 'date_scheduled')

        # Deleting field 'MedicationScheduleItem.date_start'
        db.delete_column('indivo_medicationscheduleitem', 'date_start')

        # Deleting field 'MedicationScheduleItem.date_end'
        db.delete_column('indivo_medicationscheduleitem', 'date_end')

        # Deleting field 'MedicationScheduleItem.recurrencerule_frequency'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_frequency')

        # Deleting field 'MedicationScheduleItem.recurrencerule_frequency_type'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_frequency_type')

        # Deleting field 'MedicationScheduleItem.recurrencerule_frequency_value'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_frequency_value')

        # Deleting field 'MedicationScheduleItem.recurrencerule_frequency_abbrev'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_frequency_abbrev')

        # Deleting field 'MedicationScheduleItem.recurrencerule_interval'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_interval')

        # Deleting field 'MedicationScheduleItem.recurrencerule_interval_type'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_interval_type')

        # Deleting field 'MedicationScheduleItem.recurrencerule_interval_value'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_interval_value')

        # Deleting field 'MedicationScheduleItem.recurrencerule_interval_abbrev'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_interval_abbrev')

        # Deleting field 'MedicationScheduleItem.recurrencerule_dateuntil'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_dateuntil')

        # Deleting field 'MedicationScheduleItem.recurrencerule_count'
        db.delete_column('indivo_medicationscheduleitem', 'recurrencerule_count')

        # Adding field 'Vitals.date_measured'
        db.add_column('indivo_vitals', 'date_measured', self.gf('django.db.models.fields.DateTimeField')(null=True), keep_default=False)

        # Adding field 'Vitals.unit'
        db.add_column('indivo_vitals', 'unit', self.gf('django.db.models.fields.CharField')(default=None, max_length=100), keep_default=False)

        # Adding field 'Vitals.value'
        db.add_column('indivo_vitals', 'value', self.gf('django.db.models.fields.FloatField')(default=None), keep_default=False)

        # Adding field 'Vitals.unit_abbrev'
        db.add_column('indivo_vitals', 'unit_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True), keep_default=False)

        # Adding field 'Vitals.unit_type'
        db.add_column('indivo_vitals', 'unit_type', self.gf('django.db.models.fields.CharField')(max_length=80, null=True), keep_default=False)

        # Adding field 'Vitals.unit_value'
        db.add_column('indivo_vitals', 'unit_value', self.gf('django.db.models.fields.CharField')(max_length=40, null=True), keep_default=False)

        # Deleting field 'Vitals.measured_by'
        db.delete_column('indivo_vitals', 'measured_by')

        # Deleting field 'Vitals.date_measured_start'
        db.delete_column('indivo_vitals', 'date_measured_start')

        # Deleting field 'Vitals.date_measured_end'
        db.delete_column('indivo_vitals', 'date_measured_end')

        # Deleting field 'Vitals.result_unit'
        db.delete_column('indivo_vitals', 'result_unit')

        # Deleting field 'Vitals.result_textvalue'
        db.delete_column('indivo_vitals', 'result_textvalue')

        # Deleting field 'Vitals.result_value'
        db.delete_column('indivo_vitals', 'result_value')

        # Deleting field 'Vitals.result_unit_type'
        db.delete_column('indivo_vitals', 'result_unit_type')

        # Deleting field 'Vitals.result_unit_value'
        db.delete_column('indivo_vitals', 'result_unit_value')

        # Deleting field 'Vitals.result_unit_abbrev'
        db.delete_column('indivo_vitals', 'result_unit_abbrev')

        # Deleting field 'Vitals.technique'
        db.delete_column('indivo_vitals', 'technique')


    models = {
        'indivo.accesstoken': {
            'Meta': {'object_name': 'AccessToken', '_ormbases': ['indivo.Principal']},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Share']"}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'indivo.account': {
            'Meta': {'object_name': 'Account', '_ormbases': ['indivo.Principal']},
            'account': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'failed_login_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'last_failed_login_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_login_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_state_change': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'primary_secret': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'secondary_secret': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'uninitialized'", 'max_length': '50'}),
            'total_login_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'indivo.accountauthsystem': {
            'Meta': {'unique_together': "(('auth_system', 'username'),)", 'object_name': 'AccountAuthSystem'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auth_systems'", 'to': "orm['indivo.Account']"}),
            'auth_parameters': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'auth_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.AuthSystem']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountauthsystem_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user_attributes': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'indivo.adherenceitem': {
            'Meta': {'object_name': 'AdherenceItem', '_ormbases': ['indivo.Fact']},
            'adherence': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_reported': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'nonadherence_reason': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrence_index': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'reported_by': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indivo.allergy': {
            'Meta': {'object_name': 'Allergy', '_ormbases': ['indivo.Fact']},
            'allergen_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'allergen_name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'allergen_name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'allergen_name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'allergen_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'allergen_type_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'allergen_type_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'allergen_type_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'date_diagnosed': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'diagnosed_by': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'reaction': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'specifics': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'indivo.audit': {
            'Meta': {'object_name': 'Audit'},
            'document': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'req_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'req_domain': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'req_effective_principal_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'req_headers': ('django.db.models.fields.TextField', [], {}),
            'req_ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'req_method': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'req_proxied_by_principal_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'req_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'req_view_func': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'resp_code': ('django.db.models.fields.IntegerField', [], {}),
            'resp_error_msg': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'resp_headers': ('django.db.models.fields.TextField', [], {}),
            'resp_server': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'indivo.authsystem': {
            'Meta': {'object_name': 'AuthSystem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authsystem_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'internal_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'indivo.carenet': {
            'Meta': {'unique_together': "(('name', 'record'),)", 'object_name': 'Carenet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenet_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']"})
        },
        'indivo.carenetaccount': {
            'Meta': {'unique_together': "(('carenet', 'account'),)", 'object_name': 'CarenetAccount'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'can_write': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetaccount_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'indivo.carenetautoshare': {
            'Meta': {'unique_together': "(('carenet', 'record', 'type'),)", 'object_name': 'CarenetAutoshare'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetautoshare_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.DocumentSchema']", 'null': 'True'})
        },
        'indivo.carenetdocument': {
            'Meta': {'unique_together': "(('carenet', 'document'),)", 'object_name': 'CarenetDocument'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetdocument_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'share_p': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'indivo.carenetpha': {
            'Meta': {'unique_together': "(('carenet', 'pha'),)", 'object_name': 'CarenetPHA'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetpha_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHA']"})
        },
        'indivo.document': {
            'Meta': {'unique_together': "(('record', 'external_id'),)", 'object_name': 'Document'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'content_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'digest': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'nevershare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'original': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_thread'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pha_document'", 'null': 'True', 'to': "orm['indivo.PHA']"}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'null': 'True', 'to': "orm['indivo.Record']"}),
            'replaced_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_replaced'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['indivo.StatusName']"}),
            'suppressed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'suppressed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Principal']", 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.DocumentSchema']", 'null': 'True'})
        },
        'indivo.documentprocessing': {
            'Meta': {'object_name': 'DocumentProcessing'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documentprocessing_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'processed_doc'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'indivo.documentrels': {
            'Meta': {'object_name': 'DocumentRels'},
            'document_0': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rels_as_doc_0'", 'to': "orm['indivo.Document']"}),
            'document_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rels_as_doc_1'", 'to': "orm['indivo.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.DocumentSchema']"})
        },
        'indivo.documentschema': {
            'Meta': {'object_name': 'DocumentSchema'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documentschema_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'stylesheet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stylesheet'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'indivo.documentstatushistory': {
            'Meta': {'object_name': 'DocumentStatusHistory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documentstatushistory_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'effective_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'proxied_by_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {}),
            'record': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.StatusName']"})
        },
        'indivo.equipment': {
            'Meta': {'object_name': 'Equipment', '_ormbases': ['indivo.Fact']},
            'date_started': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_stopped': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        'indivo.equipmentscheduleitem': {
            'Meta': {'object_name': 'EquipmentScheduleItem', '_ormbases': ['indivo.Fact']},
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_scheduled': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrencerule_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'recurrencerule_dateuntil': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'recurrencerule_frequency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recurrencerule_frequency_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'recurrencerule_frequency_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrencerule_frequency_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrencerule_interval': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recurrencerule_interval_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'recurrencerule_interval_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrencerule_interval_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'scheduled_by': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indivo.fact': {
            'Meta': {'object_name': 'Fact'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allergy'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allergy'", 'null': 'True', 'to': "orm['indivo.Record']"})
        },
        'indivo.immunization': {
            'Meta': {'object_name': 'Immunization', '_ormbases': ['indivo.Fact']},
            'administered_by': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'adverse_event': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'anatomic_surface': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'anatomic_surface_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'anatomic_surface_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'anatomic_surface_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'date_administered': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vaccine_expiration': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'vaccine_lot': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'vaccine_manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'vaccine_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'vaccine_type_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'vaccine_type_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'vaccine_type_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        'indivo.lab': {
            'Meta': {'object_name': 'Lab', '_ormbases': ['indivo.Fact']},
            'date_measured': ('django.db.models.fields.DateTimeField', [], {}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'first_lab_test_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'first_lab_test_value': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'first_panel_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'lab_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'lab_comments': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'lab_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'lab_type': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'non_critical_range_maximum': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'non_critical_range_minimum': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'normal_range_maximum': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'normal_range_minimum': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        },
        'indivo.machineapp': {
            'Meta': {'object_name': 'MachineApp'},
            'app_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'indivo.measurement': {
            'Meta': {'object_name': 'Measurement', '_ormbases': ['indivo.Fact']},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        'indivo.medication': {
            'Meta': {'object_name': 'Medication', '_ormbases': ['indivo.Fact']},
            'activeingredient_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'activeingredient_name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'activeingredient_name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'activeingredient_name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'activeingredient_strength_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'activeingredient_strength_unit': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'activeingredient_strength_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'activeingredient_strength_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'activeingredient_strength_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'activeingredient_strength_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amount_ordered_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'amount_ordered_unit': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'amount_ordered_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amount_ordered_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'amount_ordered_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'amount_ordered_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'datetime_expires': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'datetime_ordered': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'datetime_started': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'datetime_stopped': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'dose_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'dose_unit': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'dose_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'dose_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'dose_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'dose_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'form': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'form_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'form_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'form_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'frequency_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'frequency_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'frequency_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'indication': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'order_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'ordered_by': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'prescription_duration': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'prescription_instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'prescription_refill_info': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'reason_stopped': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'refills': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'route': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'route_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'route_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'route_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'substitution_permitted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'indivo.medicationadministration': {
            'Meta': {'object_name': 'MedicationAdministration', '_ormbases': ['indivo.Fact']},
            'amountadministered_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountadministered_unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'amountadministered_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountadministered_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'amountadministered_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountadministered_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'amountremaining_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountremaining_unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'amountremaining_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountremaining_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'amountremaining_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountremaining_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'date_administered': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_reported': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'reported_by': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        'indivo.medicationfill': {
            'Meta': {'object_name': 'MedicationFill', '_ormbases': ['indivo.Fact']},
            'amountfilled_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountfilled_unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'amountfilled_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountfilled_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'amountfilled_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountfilled_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'date_filled': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'fill_sequence_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'filled_by': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'lot_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'ndc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ndc_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'ndc_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'ndc_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'refills_remaining': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'indivo.medicationorder': {
            'Meta': {'object_name': 'MedicationOrder', '_ormbases': ['indivo.Fact']},
            'amountordered_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountordered_unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'amountordered_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountordered_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'amountordered_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'amountordered_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'date_expires': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_ordered': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'indication': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'order_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'ordered_by': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'refills': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'substitution_permitted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'indivo.medicationscheduleitem': {
            'Meta': {'object_name': 'MedicationScheduleItem', '_ormbases': ['indivo.Fact']},
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_scheduled': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'dose_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'dose_unit': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'dose_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'dose_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'dose_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'dose_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrencerule_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'recurrencerule_dateuntil': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'recurrencerule_frequency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recurrencerule_frequency_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'recurrencerule_frequency_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrencerule_frequency_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrencerule_interval': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recurrencerule_interval_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'recurrencerule_interval_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'recurrencerule_interval_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'scheduled_by': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indivo.message': {
            'Meta': {'object_name': 'Message'},
            'about_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'archived_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_type': ('django.db.models.fields.CharField', [], {'default': "'plaintext'", 'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'external_identifier': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'num_attachments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'read_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'received_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_as_recipient'", 'to': "orm['indivo.Principal']"}),
            'response_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_responses'", 'null': 'True', 'to': "orm['indivo.Message']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_as_sender'", 'to': "orm['indivo.Principal']"}),
            'severity': ('django.db.models.fields.CharField', [], {'default': "'low'", 'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indivo.messageattachment': {
            'Meta': {'unique_together': "(('message', 'attachment_num'),)", 'object_name': 'MessageAttachment'},
            'attachment_num': ('django.db.models.fields.IntegerField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messageattachment_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Message']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'saved_to_document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'indivo.nonce': {
            'Meta': {'unique_together': "(('nonce', 'oauth_type'),)", 'object_name': 'Nonce'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nonce': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'oauth_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        'indivo.notification': {
            'Meta': {'object_name': 'Notification'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'app_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notification_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notifications_sent_by'", 'to': "orm['indivo.Principal']"})
        },
        'indivo.nouser': {
            'Meta': {'object_name': 'NoUser', '_ormbases': ['indivo.Principal']},
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'})
        },
        'indivo.pha': {
            'Meta': {'object_name': 'PHA'},
            'autonomous_reason': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'callback_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'frameable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_ui': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_autonomous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': True}),
            'privacy_tou': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'schema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.DocumentSchema']", 'null': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'start_url_template': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'indivo.principal': {
            'Meta': {'object_name': 'Principal'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'principal_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indivo.problem': {
            'Meta': {'object_name': 'Problem', '_ormbases': ['indivo.Fact']},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_onset': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_resolution': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'diagnosed_by': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'})
        },
        'indivo.procedure': {
            'Meta': {'object_name': 'Procedure', '_ormbases': ['indivo.Fact']},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_performed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'provider_institution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        'indivo.record': {
            'Meta': {'object_name': 'Record'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'the_record_for_contact'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'record_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'demographics': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'the_record_for_demographics'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records_owned_by'", 'null': 'True', 'to': "orm['indivo.Principal']"})
        },
        'indivo.recordnotificationroute': {
            'Meta': {'unique_together': "(('account', 'record'),)", 'object_name': 'RecordNotificationRoute'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recordnotificationroute_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notification_routes'", 'to': "orm['indivo.Record']"})
        },
        'indivo.reqtoken': {
            'Meta': {'object_name': 'ReqToken', '_ormbases': ['indivo.Principal']},
            'authorized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'authorized_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'oauth_callback': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHA']"}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Share']", 'null': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'verifier': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'indivo.schedulegroup': {
            'Meta': {'object_name': 'ScheduleGroup', '_ormbases': ['indivo.Fact']},
            'count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'datetime_end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'datetime_scheduled': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'datetime_start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'datetime_until': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'frequency_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'frequency_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'frequency_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'scheduled_by': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indivo.sessionrequesttoken': {
            'Meta': {'object_name': 'SessionRequestToken'},
            'approved_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessionrequesttoken_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'})
        },
        'indivo.sessiontoken': {
            'Meta': {'object_name': 'SessionToken'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessiontoken_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'expires_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'})
        },
        'indivo.share': {
            'Meta': {'unique_together': "(('record', 'with_account'), ('record', 'with_pha'))", 'object_name': 'Share'},
            'authorized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'authorized_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shares_authorized_by'", 'null': 'True', 'to': "orm['indivo.Account']"}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'share_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shares'", 'to': "orm['indivo.Record']"}),
            'role_label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'with_account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shares_to'", 'null': 'True', 'to': "orm['indivo.Account']"}),
            'with_pha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shares_to'", 'null': 'True', 'to': "orm['indivo.PHA']"})
        },
        'indivo.simpleclinicalnote': {
            'Meta': {'object_name': 'SimpleClinicalNote', '_ormbases': ['indivo.Fact']},
            'chief_complaint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_of_visit': ('django.db.models.fields.DateTimeField', [], {}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'finalized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'provider_institution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'signed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'specialty_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'specialty_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'specialty_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'visit_location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'visit_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'visit_type_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'visit_type_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'visit_type_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        'indivo.statusname': {
            'Meta': {'object_name': 'StatusName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'indivo.videomessage': {
            'Meta': {'object_name': 'VideoMessage', '_ormbases': ['indivo.Fact']},
            'date_recorded': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_sent': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'file_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'from_str': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'storage_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'indivo.vitals': {
            'Meta': {'object_name': 'Vitals', '_ormbases': ['indivo.Fact']},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_measured_end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_measured_start': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'measured_by': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'result_textvalue': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'result_unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'result_unit_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'result_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'result_unit_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'result_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'technique': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['indivo']
