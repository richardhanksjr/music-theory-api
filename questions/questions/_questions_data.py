from questions.questions.intervals import (SemitonesInInterval, IntervalRaisedLoweredIs, InvertedInterval,
                                 IntervalChangedByStepBecomesQuality)
from questions.questions.major_scale_questions import SimpleScaleDegreeMajor
from questions.questions.minor_scale_questions import SimpleScaleDegreeMinor
from questions.questions.simple_questions import (SimpleIntervalIs, InvertedQualityIs, TritoneIs,
                                        CouldBePerfectInterval, TwoWaysOfSoundingIntervals,
                                        SmallestDistanceBetweenTwoPitches, SordinoMeans,
                                        TwoDifferentIntervalsSpelledDifferentlySameSound)
from questions.models import Question

questions = [SemitonesInInterval, IntervalRaisedLoweredIs, InvertedInterval, IntervalChangedByStepBecomesQuality,
             SimpleScaleDegreeMajor, SimpleScaleDegreeMinor, SimpleIntervalIs, InvertedQualityIs, TritoneIs,
             CouldBePerfectInterval, TwoWaysOfSoundingIntervals, SmallestDistanceBetweenTwoPitches, SordinoMeans,
             TwoDifferentIntervalsSpelledDifferentlySameSound]

tags = [{"name": "Interval", "questions": [SemitonesInInterval, IntervalRaisedLoweredIs, InvertedInterval, IntervalChangedByStepBecomesQuality]},
        {"name": "Interval Quality", "questions": [IntervalRaisedLoweredIs, IntervalChangedByStepBecomesQuality]},
        {"name": "Definitions", "questions": [SordinoMeans]},
        {"name": "Scale Degree Identification", "questions": [SimpleScaleDegreeMajor, SimpleScaleDegreeMinor]},
        {"name": "Minor Scale", "questions": [SimpleScaleDegreeMinor]},
        {"name": "Major Scale", "questions": [SimpleScaleDegreeMajor]}]
