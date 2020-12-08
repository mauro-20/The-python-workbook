# Widgets and Gizmos

widget_weight = 75
gizmo_weight = 112

widget_input = int(input('how many widgets do you need? '))
gizmo_input = int(input('how many gizmos do you need? '))

total_weight = widget_input*widget_weight+gizmo_input*gizmo_weight

print('the total weight of your items is %igr' %total_weight)