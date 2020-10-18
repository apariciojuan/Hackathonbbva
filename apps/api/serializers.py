from rest_framework import serializers
from apps.usuario.models import PerfilUsuario
from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr



class PerfilCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model= PerfilUsuario
        fields = ['nombre', 'apellido', 'dni', 'photo']


class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model= PerfilUsuario
        fields = ['nombre', 'apellido', 'dni', 'numero_usuario']
        read_only_fields = ('numero_usuario',)


class Base64ImageField(serializers.ImageField):
    """
    It uses base64 for encoding and decoding the contents of the file.
    """

    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                logger.error('[++++] datos en base64 serializer: {}'.format(data[0:30]))
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class BioFaceSerializer(serializers.Serializer):
    image = Base64ImageField(
        max_length=None, use_url=True
    )
    numero_usuario = serializers.CharField(
        required=True,  
        max_length=100
    )