from django import forms
from .models import Comunidad, RepresentanteFamilia, ProgresoVivienda

class ComunidadForm(forms.ModelForm):
    class Meta:
        model = Comunidad
        fields = ['nombre']  # O cualquier otro campo que tenga el modelo Comunidad

class RepresentanteFamiliaForm(forms.ModelForm):
    class Meta:
        model = RepresentanteFamilia
        fields = ['nombre', 'comunidad']  # Asumiendo que RepresentanteFamilia tiene un campo 'comunidad' que es una ForeignKey

class ProgresoForm(forms.ModelForm):
    class Meta:
        model = ProgresoVivienda
        exclude = ['promedio_progreso']  # Excluir el campo promedio del formulario
        fields = ['fecha_registro', 'estufa_mejorada',
                  'agua_potable', 'divisiones',
                  'piso',
                  'limpieza',  'muebles', 'comida_protegida',
                  
                  'plagas', 'jaulas', 'desparacitacion', 'ahorro',
                  'piscicultura', 'tuberculos',
                  'arboles_frutales', 'cerco_vivo',

                  'reciclaje', 'banio_diario',
                  'lavar_manos', 'letrina',
                  'sumidero', 'escuela',
                  'capacitaciones', 'vacunacion',
                  'peso', 'chequeo_embarazo',
                  'emergencia_embarazo']
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        # Aquí se revisa si 'representante' se pasó como argumento al formulario
        representante = kwargs.pop('representante', None)
        super(ProgresoForm, self).__init__(*args, **kwargs)
        if representante:
            # Si el representante existe, se establece el valor inicial y se oculta el campo
            self.fields['representante'].initial = representante
            self.fields['representante'].widget = forms.HiddenInput()  # Oculta el campo