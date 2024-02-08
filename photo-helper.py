"""
Generate divs and filtering tags based on image names and place them inside a html file.
"""

import os
import sys

photo_folder_path = "./Photos/"
photo_folder_path = os.fsencode(photo_folder_path)
photos_page_path = "photos.html"
photos_template_path = "photos-template.html"


def generate_photo_divs(photo_folder_path):

    tag_filter_list = set()
    div_snippet = ""

    for file in os.listdir(photo_folder_path):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg") or filename.endswith(".png"):

            file_tags = filename.split(".")[0].split("_")
            file_tags_hashtag = ["#" + tag + " " for tag in file_tags]

            main_tag = file_tags[0]

            tag_filter_list.add(main_tag)

            div_snippet += f"""
            <div class="photo-holder {main_tag}">
            <div class="photo"><img src="Photos/{filename}" style="width: 100%; text-align: center;">
            </div>
            <div class="photo-text">{''.join(file_tags_hashtag)}</div>
            </div>
            """

            continue
        else:
            continue

    tag_filter_list = list(tag_filter_list)

    return div_snippet, tag_filter_list


def generate_buttons(tag_filter_list):

    buttons = ""
    for tag_ in tag_filter_list:

        buttons += f"""
        <button class="btn" onclick="filterSelection('{tag_}')">{tag_}</button>
        """

    return buttons


def find_line(file_path, string_to_find):

    with open(photos_template_path, "r") as p_t_:

        lines = p_t_.readlines()

        for line_num in range(len(lines)):

            if string_to_find in lines[line_num]:

                return line_num


def insert_in_the_file(file, newfile, line, string_to_insert):

    with open(file, "r") as f:
        contents = f.readlines()

    contents.insert(line, string_to_insert)

    with open(newfile, "w") as f:
        contents = "".join(contents)
        f.write(contents)


# 1 generate photo divs
photo_divs, main_tags = generate_photo_divs(photo_folder_path)
buttons_div = generate_buttons(main_tags)
btn_line = find_line(photos_template_path, "<!-- PYMAGIC-BUTTON -->") + 1
photo_line = find_line(photos_template_path, "<!-- PYMAGIC-PHOTOS -->") + 2

with open(photos_template_path, "r") as f:
    contents = f.readlines()

contents.insert(btn_line, buttons_div)
contents.insert(photo_line, photo_divs)

with open(photos_page_path, "w") as f:
    contents = "".join(contents)
    f.write(contents)
