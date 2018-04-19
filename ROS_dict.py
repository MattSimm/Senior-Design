# How to map keys to a value using dictionary:
# fever_keys = ['temperature', 'flush', 'burning']
# ROS = dict.fromkeys(fever_keys, 'Fever')

# general
pain_keys = ['pain', 'achy', 'sore', 'burn', 'discomfort', 'hurt', 'irritated',
				'irritation', 'strain', 'strained']


# History: Constitutional
fever_keys = ['temperature', 'flush', 'burning', 'flushed', 'hot', 'sweat', 'sweating',
			  'temp', 'fever']

chills_keys = ['chill', 'chilled', 'chills', 'cold', 'chilly', 'cold', 'freezing',
			   'froze', 'shivering', 'shiver']

nightSweat_keys = ['sweat', 'sweating', 'sweats', 'night','nighttime', 'night time'
				   ]

weightLoss_keys = ['weight', 'loss', 'lost', 'losing', 'skinny', 'pounds', 'pound',
				   'light']

weightGain_keys = ['weight', 'pound', 'pounds', 'gained', 'gaining', 'gain', 'fat',
				   'heavy', 'hefty']

changeInAppetite_keys = ['loss', 'gain', 'appetizing', 'appetite', 'hungry', 'full',
						 'craving', 'stomach']

fatigue_keys = ['lathargic', 'weak', 'tired', 'exhausted', 'faint', 'heavy', 'slow',
				'burnt out', 'drag', 'worn', 'tedious']

somnolence_keys = ['sleepy', 'tired', 'drowsy', 'doziness', 'dozed', 'out of it',
				   'sluggish', 'oversleep', 'overslept', 'sleep']


# Hisotry: Eyes

visionLoss_keys = ['blurred', 'losing', 'lost', 'difficult', 'hard', 'tough', 'see',
				   'unclear', 'muddy', 'vision', 'obscure', 'foggy', 'cloudy', 'hazy'
				   'sight', 'vision', 'perception']

doubleVision_keys = ['double', 'cross', 'vision', 'two', 'multiple', 'seeing', 'sight',
					 'perception']

eyePain_keys = pain_keys + ['eye', 'eyes']

redEye_keys = ['red', 'blood', 'shot', 'pink', 'irritated']

# History: Ears, nose, mouth, throat

earPain_keys = pain_keys + ['ear', 'ears']

earDischarge_keys = ['ear', 'ears', 'gunk', 'stuff', 'wax', 'fluid', 'goo', 'crap', 'crud',
					 'discharge']

hearingLoss_keys = ['deaf', 'deafening', 'hard', 'difficult', 'losing', 'loss', 'trouble', 'impair',
					'hear', 'hearing', 'ear', 'ears']

earRinging_keys = ['ring', 'ringing', 'tinnitus', 'buzzing', 'hissing', 'chirping', 'whistling', 'humming',
				   'clicking', 'ring', 'ear', 'ears']

nasalBleeding_keys = ['nose', 'bleed', 'blood', 'bloody', 'epistaxis']

sinusPressure_keys = ['clogged', 'stuffed', 'breath', 'hard', 'nose']

soreThroat_keys = ['throat', 'raw', 'sore', 'achy', 'hurt', 'hard', 'swallow', 'scratchy', 'tender',
				   'pain'] + pain_keys

oralSores_keys = ['sore', 'abscess', 'lesion']

toothPain_keys = ['tooth', 'teeth', 'ache', 'mouth'] + pain_keys

bleedingGums_keys = ['gum', 'gums', 'teeth', 'tooth', 'blood', 'bleeding', 'sore',
					 'bleed']

hoarseVoice_keys = ['voice', 'speech', 'talk', 'sound', 'deep', 'hoarse', 'horse', 'raspy',
					'gravelly', 'scratchy', 'cracked', 'dry', 'croak', 'croaky', 'gruff',
					'rough', 'husky', 'growly', 'growl']

neckPain_keys = ['neck', 'head', 'throat'] + pain_keys

# History: Cardiovascular

chestPain_keys = ['chest', 'heart', 'sharp', 'dull', 'burn', 'burning', 'stabbing', 'crushing',
				  'chrush', 'stab', 'stabbed'] + pain_keys

palpatations_keys = ['heart', 'heartbeat', 'fast', 'hard', 'weird', 'skip', 'skipping', 'flutter',
					 'fluttering', 'abnormal', 'irregular', 'racing']

legSwelling_keys = ['leg', 'legs', 'thigh', 'calf', 'calves', 'ankle', 'ankles', 'swollen',
					'swell', 'swolling', 'puffy', 'puffiness', 'stretch', 'stretched', 'raised',
					'bloated', 'big', 'knee', 'knees']

legPainWalking_keys = ['leg', 'legs', 'thigh', 'calf', 'calves', 'ankle', 'ankles', 'knees', 'knee',
						'walk', 'cramp', 'walking', 'jog', 'jogging','weak', 'exercise', 'pain'] + pain_keys


# History: Respiratory

cough_keys = ['cough', 'hacking', 'blood', 'coughing', 'hack', 'bark', 'coughed',
			  'barking']

wheezing_keys = ['wheeze', 'wheezing', 'gasp', 'gasping', 'hiss', 'hissing', 'rough', 'heavily',
				 'whistle', 'whistling', 'rattling']

snoring_keys = ['sleeping', 'sleep', 'asleep', 'snore', 'snoring', 'snorting', 'snort',
				'snorting', 'heavy']

shortnessOfBreath_keys = ['breath', 'breathing', 'short', 'hard', 'shallow', 'winded',
						  'shortness', 'out', 'gasping', 'gasp']

# History: Gastrointestinal

nausea_keys = ['quesy', 'puke', 'puking', 'throw', 'barf', 'barfing', 'hurl', 'hurling',
			   'regurgitate', 'upset', 'stomach']

diarrhea_keys = ['diarrhea']

constipation_keys = ['blocked', 'backed', 'obstruction', 'clogged']

abdominalPain_keys = ['abs', 'abnominal', 'stomach', 'tummy', 'belly', 'gut', 'intestine', 'intestinal'
					  'colon', 'bladder', 'spleen'] + pain_keys

redStool_keys = ['poop', 'shit', 'crap', 'fecal', 'stool', 'blood', 'red', 'pink', 'bright']

blackStool_keys = ['poop', 'shit', 'crap', 'fecal', 'stool', 'black', 'tar', 'tarry', 'gray', 'dark',
				   'grey']

stoolIncontinence_keys = ['poop', 'shit', 'crap', 'fecal', 'stool', 'accident', 'incontinence']

# Genitourinary

pelvicPain_keys = ['pelvis', 'bladder', 'abdomen', 'stomach', 'appendix', 'colon', 'bowel',
				  'lower'] + pain_keys

burningUrination_keys = ['pain', 'painful', 'pee', 'urinate', 'bathroom', 'go', 'piss', 'restroom',
						'bathroom'] + pain_keys

frequentUrination_keys = ['pee', 'piss', 'urinate', 'bathroom', 'restroom', 'go', 'constant', 'time', 'all',
						  'persistent', 'non', 'stop', 'constant', 'constantly']

urgentUrination_keys = ['pee', 'piss', 'urinate', 'bathroom', 'restroom', 'go', 'urge', 'bad', 'sudden',
						'unexpected', 'nowhere', 'out of', 'random', 'instant', 'accident']


bloodInUrine_keys = ['pee', 'piss', 'urinate', 'blood', 'red']

incompleteBladderEmptying_keys = ['incomplete', 'dribbling']

urinaryIncontinence_keys = ['no control', 'random', 'accident', 'involuntary']

sexuallyTransmittedDisease_keys = ['std', 'sexually transmitted disease']

menPrivates_keys = ['testicular', 'testicle', 'scrotum', 'erectile dysfunction']

womenPrivates_keys = ['menstrual', 'period']

# History: Musculoskeletal

bonePain_keys = ['bone', 'bones'] + pain_keys

jointPain_keys = ['joint', 'joints', 'tendon', 'arthritis', 'tennis elbow'] + pain_keys

musclePain_keys = ['muscle', 'muscles'] + pain_keys

# History: Skin

rashOrMole_keys = ['rash', 'irritation', 'skin', 'mole', 'breaking out', 'hives']

skinItch_keys = ['skin', 'itch', 'itchy', 'scratch', 'scratchy']

breastLump_keys = ['breast', 'lump', 'bump', 'growth', 'mass']

breastPain_keys = ['breast'] + pain_keys

nippleDischarge_keys = ['nipple', 'discharge', 'ooze', 'seeping']

hairLoss_keys = ['hair', 'loss', 'losing', 'bald', 'balding']

# History: Neurologic

headache_keys = ['headache', 'head', 'migraine']

muscleWeakness_keys = ['muscles', 'muscle', 'weak', 'fatigue', 'fatigued']

sensationChanges_keys = ['numb', 'numbness', 'coldness', 'crawling', 'prickling', 'burning',
						 'tingling', 'tickling', 'pins and needles']

memoryLoss_keys = ['memory loss', 'forget', 'memory']

seizure_keys = ['seizure', 'epiliepsy']

dizziness_keys = ['light headed', 'room spinning', 'faint', 'fainting', 'imbalance', 'dizzy', 'dizziness',
				  'fainted']

# History: Psychiatric

anxiety_keys = ['restless', 'nervous', 'nervousness', 'shaking', 'overwhelmed', 'shaky', 'dizzy', 'fear',
				]

sadness_keys = ['sad', 'depressed', 'down', 'unhappy', 'miserable']

irritability_keys = ['irritable', 'irritated', 'on edge', 'annoyed', 'short temper', 'testy']

insomnia_keys = ['insomnia', 'cant sleep', 'trouble sleeping']

suicidal_keys = ['suicide', 'suicidal']

# History: Endocrine

heatAndColdIntolerance_keys = ['hot', 'cold', 'intolerable', 'uncomfortable']

excessiveThirst_keys = ['thirsty' , 'constant', 'always thirsty', 'thrist']

excessiveHunger_keys = ['hungry' , 'constant', 'always hungry', 'hunger']

lymphNodeEnlargement_keys = ['lymph', 'lymph node', 'enlargement', 'big']

easyBleedingAndBruising_keys = ['easy', 'bruise', 'bleeding']

# History: Allergic or immunologic

hives_keys = ['lesions', 'scratching', 'red', 'rash']

seasonalAllergies_keys = ['seasonal', 'allergies', 'sneezing' ,'runny nose', 'watery eyes', 'itchy']

hivExposure_keys = ['HIV', 'hiv']


