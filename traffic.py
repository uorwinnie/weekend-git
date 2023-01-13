print("Choose a colour for pedestrian traffic light. 'Red' 'Green'")
human=input('Traffic light colour for human:')
print("Choose a colour for traffic light. 'Red' 'Green' Yellow' ")
car=input('Traffic light colour for cars:')
if human=='Green':
  if car=='Red':
    print('Human are safe to cross the road.')
    print('Cars have to stop.')
  elif car=='Yellow':
    print('Wait!The cars will stop soon.Then you can cross the road.')
    print('Cars have be slow down. The traffic will be red in very short moment.')
  elif car=='Green':
    print('DON\'T CROSS THE ROAD! The cars are coming. This pedestrian traffic must be broken.')
else:
    if car=='Red':
        print('This car traffic must be broken.')
        print('Cars can go when human are stopping and the pedestrian traffic light is red.')
    elif car=='Yellow':
        print('Cars have be slow down. The traffic will be red in very short moment.')
        print('When the light turns red, people will cross the road.')
    elif car=='Green':
        print('Cars can go.')