# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Passport'
        db.create_table('core_passport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birthday', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('date_of_list', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('registration_type', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('reqistration_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('no_reqistration_reason', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fact_live_address_in_mo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fact_live_address_outside_mo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('place_of_first_find', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('family_status', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('children', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=255)),
            ('has_real_estate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('real_estate_EGRP', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('real_estate_not_EGRP', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('form_of_care', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spokesman_data', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('provision_of_employment_type', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('employment_place', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('education_type', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('name_institution_of_education', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('vacation', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('army', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('jail', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_of_service_expired', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('annotation', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('core', ['Passport'])


    def backwards(self, orm):
        # Deleting model 'Passport'
        db.delete_table('core_passport')


    models = {
        'core.passport': {
            'Meta': {'object_name': 'Passport'},
            'annotation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'army': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'children': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '255'}),
            'date_of_list': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_of_service_expired': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'education_type': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'employment_place': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fact_live_address_in_mo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fact_live_address_outside_mo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'family_status': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'form_of_care': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'has_real_estate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_institution_of_education': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'no_reqistration_reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'place_of_first_find': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'provision_of_employment_type': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'real_estate_EGRP': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'real_estate_not_EGRP': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registration_type': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'reqistration_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spokesman_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vacation': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['core']