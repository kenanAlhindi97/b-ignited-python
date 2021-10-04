class Tag:
    def __init__(self, tag_id, tag_name):
        self.tag_name = tag_name
        self.tag_id = tag_id

    def to_json(self):
        return {
            "id": self.tag_id,
            "name": self.tag_name
        }


class Pet:
    def __init__(self, name, pet_id, category, cat_id, image_urls, status, tags):
        self.name = name
        self.pet_id = pet_id
        self.category = category
        self.cat_id = cat_id
        self.image_urls = image_urls
        self.status = status
        self.tags = tags

    def to_json(self):
        return {
            "id": self.pet_id,
            "name": self.name,
            "category": {
                "id": self.cat_id,
                "name": self.category
            },
            "photoUrls": self.image_urls,
            "tags": self.tags,
            "status": self.status
        }
