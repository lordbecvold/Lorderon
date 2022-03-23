#Lorderon Client Dev by Lordbecvold
import item
default_grade_need_count = [5, 5, 5, 5]
default_grade_fee = [3000, 4000, 5000, 6000]
default_step_need_count = [5, 5, 5, 5]
default_step_fee = [3000, 4000, 5000, 6000]
strength_fee = {item.MATERIAL_DS_REFINE_NORMAL : 3000, item.MATERIAL_DS_REFINE_BLESSED : 4000, item.MATERIAL_DS_REFINE_HOLLY : 5000,}
default_strength_max_table = [[2, 2, 3, 3, 4], [3, 3, 3, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 5], [4, 4, 4, 5, 6],]
default_refine_info = {"grade_need_count" : default_grade_need_count, "grade_fee" : default_grade_fee, "step_need_count" : default_step_need_count, "step_fee" : default_step_fee, "strength_max_table" : default_strength_max_table,}
dragon_soul_refine_info = {11 : default_refine_info, 12 : default_refine_info, 13 : default_refine_info,14 : default_refine_info, 15 : default_refine_info, 16 : default_refine_info,}
