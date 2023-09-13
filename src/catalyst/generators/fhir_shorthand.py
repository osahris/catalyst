import json

def generate_fhir_shorthand(metadata,output_directory):
    print("Generating FHIR Shorthand files...")
    print("Output directory: " + output_directory)

    # loop through classes in metadata
    for class_name in metadata["classes"]:
        print("Generating FHIR Shorthand for class: " + class_name)
        class_data = metadata["classes"][class_name]

        # create a file for the class
        file_name = output_directory + "/" + class_name + ".fsh"

        # open the file for writing
        with open(file_name, "wt") as file:
            file.write("Profile: " + class_name + "\n")
            file.write("Id: " + class_name + "\n")
            file.write("Parent: " + class_data["fhir_parent"] + "\n")
            if ("ShortDescription" in class_data) and ("en" in class_data["ShortDescription"]):
                file.write("Description: " + class_data["ShortDescription"]["en"] + "\n")

            # loop through the class variables
            for class_var in class_data["variables"]:
                if "fhir_attribute" in class_var:
                    if "fhir_cardinality" in class_var:
                        file.write("* " + class_var["fhir_attribute"] + " " + class_var["fhir_cardinality"] + "\n")
                    var_short_desc = metadata["vars"][class_var["var"]]["ShortDescription"]["en"]
                    file.write("* " + class_var["fhir_attribute"] + " ^short =  " + json.dumps(var_short_desc) + "\n")