import sound, time

for effect in ['Click_1', 'Click_2', 'Coin_2', 'Coin_5','Piano_G4#','Woosh_2','Woosh_1','Spaceship','Shot','Pulley','Jump','Footstep','Footstep','Footstep','Error','Ding_1','Ding_2','Ding_3','Crashing','Drums_16','Drums_15','Drums_14','Drums_13','Drums_13','Drums_13','Coin_1','Coin_2','Coin_3','Coin_4','Coin_5','Explosion_1','Explosion_2','Explosion_3','Explosion_4','Explosion_5','Explosion_6','Explosion_7','Hit_1','Hit_2','Hit_3','Hit_4','Jump_1','Jump_2','Jump_3','Jump_4','Jump_5','Laser_1','Laser_2','Laser_3','Laser_4','Laser_5','Laser_6','Powerup_1','Powerup_2','Powerup_3','Piano_G4#']:
			sound.load_effect(effect)
			sound.play_effect(effect)
			time.sleep(0.5)


notes = 'C3', 'D3', 'E3', 'C3'
for note in notes:
	sound.play_effect('Piano_' + note)
	time.sleep(0.5)

