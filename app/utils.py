from bson import ObjectId

def serialize_document(document):
   return {
      **document,
        "_id": str(document["_id"]),
   }