from google.appengine.ext import ndb


class Sample(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    created_date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def add(cls, name, description):
        sample = cls(name=name, description=description)
        sample.put()
        return sample

    @classmethod
    def get_all(cls):
        return cls.query().fetch()
