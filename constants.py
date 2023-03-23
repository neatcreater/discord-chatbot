import re

# constants
num_of_characters_to_keep = 2000

# regex
html_tag_pattern = re.compile(r"<.*?>")
multi_line_pattern = re.compile(r"\n+")
multi_space_pattern = re.compile(r"(  )")
    
# repl is short for replacement
repl_empty_str = ""
repl_br_tag = "<br>"
repl_span_tag_multispace = '<span class="chat_wrap_space">  <span>'