import itertools
import mimetools
import mimetypes
import urllib2
import json


class Prediction:
    def __init__(self, api_secret, model_id):
        self.url = "https://www.mateverse.com/v1/predict/"
        self.api_secret = api_secret
        self.model_id = model_id

    def predict(self, values):
        form = MultiPartForm()
        form.add_field('api_secret', self.api_secret)
        form.add_field('model_id', self.model_id)
        form.add_field('values', values)

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
        self.boundary = mimetools.choose_boundary()
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
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
    model_id = '****'

    # This should contain all values required for prediction in a valid json format
    values = [{"column_name": "*****", "column_value": "***"},
              {"column_name": "*****", "column_value": "***"},
              {"column_name": "*****", "column_value": "***"},
              {"column_name": "*****", "column_value": "***"}]

    # Change values to a string
    values = json.dumps(values)

    # Creating a class instance and passing in the api_secret and model_id to it
    prediction = Prediction(api_secret, model_id)

    # Passing in values to the predict function
    response = prediction.predict(values=values)

    print response
