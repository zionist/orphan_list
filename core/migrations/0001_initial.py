# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Passport'
        db.create_table(u'core_passport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('order_allegation_date_and_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('order_UMSO_conclusion_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('order_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('order_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('order_of_hiring_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('order_of_hiring_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('document', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('document_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('document_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('document_issue', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('registration_type', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('registration_address_region', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
            ('registration_address_mo', self.gf('django.db.models.fields.CharField')(max_length=409, blank=True)),
            ('registration_address_address', self.gf('django.db.models.fields.CharField')(max_length=10000, blank=True)),
            ('registration_no_reqistration_reason', self.gf('django.db.models.fields.CharField')(max_length=10000, blank=True)),
            ('lowful_status', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('lowful_status_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lowful_status_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('lowful_status_invalidity', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('form_of_care_spokesman_data', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('family_status', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('family_status_children', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('estate_has_estate', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('estate_cant_live_date_of_order', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('estate_cant_live_order_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('job_type_of_job', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('job_how_hired', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('job_job_place', self.gf('django.db.models.fields.CharField')(max_length=10000, blank=True)),
            ('job_eduction_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('job_education_house', self.gf('django.db.models.fields.CharField')(max_length=10000, blank=True)),
            ('job_other', self.gf('django.db.models.fields.CharField')(max_length=10000, blank=True)),
            ('job_started', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('job_finished', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lodging_accordance', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('lodging_how_gained', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('lodging_house_or_flat', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('lodging_square', self.gf('django.db.models.fields.CharField')(max_length=2048, blank=True)),
        ))
        db.send_create_signal('core', ['Passport'])


    def backwards(self, orm):
        # Deleting model 'Passport'
        db.delete_table(u'core_passport')


    models = {
        'core.passport': {
            'Meta': {'object_name': 'Passport'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'document_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'document_issue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'document_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'estate_cant_live_date_of_order': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'estate_cant_live_order_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'estate_has_estate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'family_status': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'family_status_children': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'form_of_care_spokesman_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_education_house': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'blank': 'True'}),
            'job_eduction_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'job_finished': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'job_how_hired': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'job_job_place': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'blank': 'True'}),
            'job_other': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'blank': 'True'}),
            'job_started': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'job_type_of_job': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lodging_accordance': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lodging_house_or_flat': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lodging_how_gained': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lodging_square': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'lowful_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lowful_status_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lowful_status_invalidity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lowful_status_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_UMSO_conclusion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'order_allegation_date_and_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'order_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'order_of_hiring_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'order_of_hiring_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'registration_address_address': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'blank': 'True'}),
            'registration_address_mo': ('django.db.models.fields.CharField', [], {'max_length': '409', 'blank': 'True'}),
            'registration_address_region': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'registration_no_reqistration_reason': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'blank': 'True'}),
            'registration_type': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']