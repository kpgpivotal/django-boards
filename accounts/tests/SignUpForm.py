# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:35:32 2019

@author: kisho_lhokk3h
"""

from django.test import TestCase
from ..forms import SignUpForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
        
        
        
        