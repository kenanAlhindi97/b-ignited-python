import sys
import requests
import pet

if __name__ == '__main__':

    images = ["https://photos.app.goo.gl/iUEjSbPmn7gxYqxP7", "https://photos.app.goo.gl/GhtEYis8GQnWiQoG9"]
    tag1 = pet.Tag(1, "cute")
    tag2 = pet.Tag(2, "regal")
    tags = [tag1.to_json(), tag2.to_json()]

    my_pet = pet.Pet("chips", 1794, "Dog", 1, images, "available", tags)

    post_response = requests.post("https://petstore3.swagger.io/api/v3/pet", json=my_pet.to_json())
    if post_response.status_code != 200:
        sys.exit("Error : " + str(post_response.content))
    print("pet posted successfully")

    get_response = requests.get("https://petstore3.swagger.io/api/v3/pet/" + str(my_pet.pet_id))
    if get_response.status_code != 200:
        sys.exit("Error :" + str(get_response.content))

    for key in get_response.json():

        local_property = my_pet.to_json()[key]
        server_property = get_response.json()[key]

        if local_property != server_property:
            print("local property: " + local_property)
            print("server property:" + server_property)
            sys.exit("Error : validation failed")

    print("posted pet successfully validated against local pet")
