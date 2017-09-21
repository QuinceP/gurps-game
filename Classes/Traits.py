from enum import Enum


class ReactionCategories(Enum):
    OWN_RACE = 'OWN_RACE'
    SIMILAR_RACE = 'SIMILAR_RACE'
    DISSIMILAR_RACE = 'DISSIMILAR_RACE'
    SAME_GENDER = 'SAME_GENDER'
    OTHER_GENDER = 'OTHER_GENDER'
    WILD_ANIMAL = 'WILD_ANIMAL'
    TAME_ANIMAL = 'TAME_ANIMAL'
    INTELLIGENT_CREATURE = 'INTELLIGENT_CREATURE'
    SAME_FAITH = 'SAME_FAITH'
    RESPECTS_FAITH = 'RESPECTS_FAITH'


class Modifier:
    def __init__(self, name, level, points, affected):
        self.name = name
        self.level = level
        self.points = points
        self.affected = affected


class Traits:
    def __init__(self, charisma_level):
        self.charisma_level = charisma_level
        #self.cleric_level = cleric_level

        image = {
            'appearance': {
                'hideous': Modifier(
                    'hideous', 1, -20, {
                        ReactionCategories.OWN_RACE: -4,
                        ReactionCategories.SIMILAR_RACE: -4
                    }),
                'ugly': Modifier(
                    'ugly', 1, -10, {
                        ReactionCategories.OWN_RACE: -2,
                        ReactionCategories.SIMILAR_RACE: -2
                    }),
                'unattractive': Modifier(
                    'unattractive', 1, -5, {
                        ReactionCategories.OWN_RACE: -1
                    }),
                'average': Modifier(
                    'average', 1, 0, {}),
                'attractive': Modifier(
                    'attractive', 1, 5, {
                        ReactionCategories.OWN_RACE: 1
                    }),
                'beautiful': Modifier(
                    'beautiful', 1, 15, {
                        ReactionCategories.OWN_RACE: 4,
                        ReactionCategories.SIMILAR_RACE: 2
                    }),
                'very_beautiful': Modifier(
                    'very_beautiful', 1, 25, {
                        ReactionCategories.OWN_RACE: 6,
                        ReactionCategories.SIMILAR_RACE: 2
                    }),
            },
            'charisma': Modifier(
                'charisma', self.charisma_level, self.charisma_level * 5,
                {ReactionCategories.INTELLIGENT_CREATURE: self.charisma_level}),
            'fat': {
                'overweight': Modifier('overweight', 1, -5, {
                    ReactionCategories.OWN_RACE: -1,
                }),
                'fat': Modifier('fat', 1, -10, {
                    ReactionCategories.OWN_RACE: -1,
                    ReactionCategories.SIMILAR_RACE: -1
                }),
                'extremely_fat': Modifier('extremely_fat', 1, -20, {
                    ReactionCategories.OWN_RACE: -2,
                    ReactionCategories.SIMILAR_RACE: -2,
                }),
            },
            'skinny': Modifier('skinny', 1, -5, {}),
            'voice': Modifier('voice', 1, 10, {ReactionCategories.INTELLIGENT_CREATURE})
        }

        # social = {
        #     #'cleric': Modifier('cleric', cleric_level, cleric_level * 5, {}),
        #
        # }

        wealth = {
            'broke': Modifier('broke', 1, -25, {}),
            'poor': Modifier('poor', 1, -15, {}),
            'struggling': Modifier('struggling', 1, -10, {}),
            'average': Modifier('average', 1, 0, {}),
            'comfortable': Modifier('comfortable', 1, 10, {}),
            'wealthy': Modifier('wealthy', 1, 20, {}),
            'very_wealthy': Modifier('very_wealthy', 1, 30, {}),
            'filthy_rich': Modifier('filthy_rich', 1, 50, {}),
        }
