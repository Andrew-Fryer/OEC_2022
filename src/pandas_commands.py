import pandas as pd

def get_child_frame(parent_id,all_possible_children):
    return all_possible_children[all_possible_children.iloc[:,6].eq(parent_id)]