import itertools
import mimetools
import mimetypes
import urllib2
import codecs


class Prediction:
    def __init__(self, api_secret, model_id):
        self.url = "https://www.mateverse.com/v1/predict/"
        self.api_secret = api_secret
        self.model_id = model_id

    def predict(self, image_url=None, file_paths=None, limit=5):
        form = MultiPartForm()
        form.add_field('api_secret', self.api_secret)
        form.add_field('model_id', self.model_id)
        form.add_field('limit', str(limit))

        if image_url is not None:
            # This post parameter is common request for both Images and Text based models
            # If images, send an url of an image
            # If text, send a text sample(sentence or paragraph or article)
            form.add_field('sampleURLText', image_url)

        if file_paths is not None:
            for file_path in file_paths:
                form.add_file('file', file_path, fileHandle=codecs.open(file_path, "rb"))

        request = urllib2.Request(self.url)
        request.add_header('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                         '(KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')
        body = str(form)
        request.add_header('Content-type', form.get_content_type())
        request.add_header('Content-length', len(body))
        request.add_data(body)

        # Response from server
        response = urllib2.urlopen(request).read()

        return response


class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, body))
        return

    def __str__(self):
        parts = []
        part_boundary = '--' + self.boundary

        # Add the form fields
        parts.extend(
            [part_boundary,
             'Content-Disposition: form-data; name="%s"' % name,
             '',
             value,
             ]
            for name, value in self.form_fields
        )

        # Add the files to upload
        parts.extend(
            [part_boundary,
             'Content-Disposition: file; name="%s"; filename="%s"' % \
             (field_name, filename),
             'Content-Type: %s' % content_type,
             '',
             body,
             ]
            for field_name, filename, content_type, body in self.files
        )

        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)


if __name__ == '__main__':
    # Put your api_secret key here
    api_secret = '**********************'

    # Put the id of the model that you want to use for prediction
    model_id = '**'

    # The images list will contain paths to all the images
    # on which you want to make the prediction
    file_paths = ['path_to_image1/image1.jpeg', 'path_to_image2/image2.jpeg']

    # Url of an image
    image_url = 'url to a public image'

    # Limit number of top predictions for this request
    limit = 5

    # Creating a class instance and passing in the api_secret and model_id to it
    prediction = Prediction(api_secret, model_id)

    # Passing in the list of images to the predict function
    response = prediction.predict(image_url=image_url, file_paths=file_paths, limit=limit)

    print response
