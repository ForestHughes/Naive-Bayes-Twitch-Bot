from collections import defaultdict
import glob
import re
import scipy.io

# ************* Features *************

# Features that look for certain words
def freq_pain_feature(text, freq):
    return float(freq['pain'])

def freq_private_feature(text, freq):
    return float(freq['private'])

def freq_bank_feature(text, freq):
    return float(freq['bank'])

def freq_money_feature(text, freq):
    return float(freq['money'])

def freq_drug_feature(text, freq):
    return float(freq['drug'])

def freq_spam_feature(text, freq):
    return float(freq['spam'])

def freq_prescription_feature(text, freq):
    return float(freq['prescription'])

def freq_creative_feature(text, freq):
    return float(freq['creative'])

def freq_height_feature(text, freq):
    return float(freq['height'])

def freq_featured_feature(text, freq):
    return float(freq['featured'])

def freq_differ_feature(text, freq):
    return float(freq['differ'])

def freq_width_feature(text, freq):
    return float(freq['width'])

def freq_other_feature(text, freq):
    return float(freq['other'])

def freq_energy_feature(text, freq):
    return float(freq['energy'])

def freq_business_feature(text, freq):
    return float(freq['business'])

def freq_message_feature(text, freq):
    return float(freq['message'])

def freq_volumes_feature(text, freq):
    return float(freq['volumes'])

def freq_revision_feature(text, freq):
    return float(freq['revision'])

def freq_path_feature(text, freq):
    return float(freq['path'])

def freq_meter_feature(text, freq):
    return float(freq['meter'])

def freq_memo_feature(text, freq):
    return float(freq['memo'])

def freq_planning_feature(text, freq):
    return float(freq['planning'])

def freq_pleased_feature(text, freq):
    return float(freq['pleased'])

def freq_record_feature(text, freq):
    return float(freq['record'])

def freq_out_feature(text, freq):
    return float(freq['out'])

# Features that look for certain characters
def freq_semicolon_feature(text, freq):
    return text.count(';')

def freq_dollar_feature(text, freq):
    return text.count('$')

def freq_sharp_feature(text, freq):
    return text.count('#')

def freq_exclamation_feature(text, freq):
    return text.count('!')

def freq_para_feature(text, freq):
    return text.count('(')

def freq_bracket_feature(text, freq):
    return text.count('[')

def freq_and_feature(text, freq):
    return text.count('&')

# --------- Add your own feature methods ----------
def example_feature(text, freq):
    return int('example' in text)
    
def freq_same_feature(text, freq):
    return text.count('same')

def freq_zas_feature(text, freq):
    return text.count('zas')

def freq_its_feature(text, freq):
    return text.count('its')

def freq_because_feature(text, freq):
    return text.count('because')

def freq_BibleThump_feature(text, freq):
    return text.count('BibleThump')

def freq_PogChamp_feature(text, freq):
    return text.count('PogChamp')

def freq_harrdddd_feature(text, freq):
    return text.count('harrdddd')

def freq_Kappa_feature(text, freq):
    return text.count('Kappa')

def freq_thats_feature(text, freq):
    return text.count('thats')

def freq_what_feature(text, freq):
    return text.count('what')

def freq_she_feature(text, freq):
    return text.count('she')

def freq_said_feature(text, freq):
    return text.count('said')

def freq_whatss_feature(text, freq):
    return text.count("what's")

def freq_the_feature(text, freq):
    return text.count('the')

def freq_difference_feature(text, freq):
    return text.count('difference')

def freq_1_feature(text, freq):
    return text.count('1')

def freq_star_feature(text, freq):
    return text.count('star')

def freq_whether_feature(text, freq):
    return text.count('whether')

def freq_you_feature(text, freq):
    return text.count('you')

def freq_skip_feature(text, freq):
    return text.count('skip')

def freq_DDD_feature(text, freq):
    return text.count('DDD')

def freq_and_feature(text, freq):
    return text.count('and')

def freq_0_feature(text, freq):
    return text.count('0')

def freq_lmfao_feature(text, freq):
    return text.count('lmfao')

def freq_Keepo_feature(text, freq):
    return text.count('Keepo')

def freq_King_feature(text, freq):
    return text.count('King')

def freq_Dedede_feature(text, freq):
    return text.count('Dedede')

def freq_troll_feature(text, freq):
    return text.count('troll')

def freq_real_feature(text, freq):
    return text.count('real')

def freq_just_feature(text, freq):
    return text.count('just')

def freq_do_feature(text, freq):
    return text.count('do')

def freq_lblj_feature(text, freq):
    return text.count('lblj')

def freq_for_feature(text, freq):
    return text.count('for')

def freq_as_feature(text, freq):
    return text.count('as')

def freq_long_feature(text, freq):
    return text.count('long')

def freq_can_feature(text, freq):
    return text.count('can')

def freq_To_feature(text, freq):
    return text.count('To')

def freq_gain_feature(text, freq):
    return text.count('gain')

def freq_speed_feature(text, freq):
    return text.count('speed')

def freq_You_feature(text, freq):
    return text.count('You')

def freq_mean_feature(text, freq):
    return text.count('mean')

def freq_this_feature(text, freq):
    return text.count('this')

def freq_SBLJ_feature(text, freq):
    return text.count('SBLJ')

def freq_keep_feature(text, freq):
    return text.count('keep')

def freq_saying_feature(text, freq):
    return text.count('saying')

def freq_LBLJ_feature(text, freq):
    return text.count('LBLJ')

def freq_FailFish_feature(text, freq):
    return text.count('FailFish')

def freq_duuuude_feature(text, freq):
    return text.count('duuuude')

def freq_LOLOLOLOL_feature(text, freq):
    return text.count('LOLOLOLOL')

def freq_if_feature(text, freq):
    return text.count('if')

def freq_I_feature(text, freq):
    return text.count('I')

def freq_bj_feature(text, freq):
    return text.count('bj')

def freq_PedoBear_feature(text, freq):
    return text.count('PedoBear')

def freq_once_feature(text, freq):
    return text.count('once')

def freq_fly_feature(text, freq):
    return text.count('fly')

def freq_over_feature(text, freq):
    return text.count('over')

def freq_hold_feature(text, freq):
    return text.count('hold')

def freq_up_feature(text, freq):
    return text.count('up')

def freq_metroid_feature(text, freq):
    return text.count('metroid')

def freq_funny_feature(text, freq):
    return text.count('funny')

def freq_Indeed_feature(text, freq):
    return text.count('Indeed')

def freq_FuzzyRNG_feature(text, freq):
    return text.count('FuzzyRNG')

def freq_question_feature(text, freq):
    return text.count('?')

def freq_sub_feature(text, freq):
    return text.count('sub')

def freq_sf5_feature(text, freq):
    return text.count('sf5')

def freq_Thats_feature(text, freq):
    return text.count('That\'s')

def freq_legitiment_feature(text, freq):
    return text.count('legitiment')

def freq_question_feature(text, freq):
    return text.count('question')

def freq_called_feature(text, freq):
    return text.count('called')

def freq_clear_feature(text, freq):
    return text.count('clear')

def freq_wow_feature(text, freq):
    return text.count('wow')

def freq_so_feature(text, freq):
    return text.count('so')

def freq_DansGame_feature(text, freq):
    return text.count('DansGame')

def freq_race_feature(text, freq):
    return text.count('race')

def freq_right_feature(text, freq):
    return text.count('right')

def freq_Now_feature(text, freq):
    return text.count('Now')


# Generates a feature vector
def generate_feature_vector(text, freq):
    feature = []
    feature.append(len(text.split())) #always nonzero, number of words in message
    feature.append(freq_pain_feature(text, freq))
    feature.append(freq_private_feature(text, freq))
    feature.append(freq_bank_feature(text, freq))
    feature.append(freq_money_feature(text, freq))
    feature.append(freq_drug_feature(text, freq))
    feature.append(freq_spam_feature(text, freq))
    feature.append(freq_prescription_feature(text, freq))
    feature.append(freq_creative_feature(text, freq))
    feature.append(freq_height_feature(text, freq))
    feature.append(freq_featured_feature(text, freq))
    feature.append(freq_differ_feature(text, freq))
    feature.append(freq_width_feature(text, freq))
    feature.append(freq_other_feature(text, freq))
    feature.append(freq_energy_feature(text, freq))
    feature.append(freq_business_feature(text, freq))
    feature.append(freq_message_feature(text, freq))
    feature.append(freq_volumes_feature(text, freq))
    feature.append(freq_revision_feature(text, freq))
    feature.append(freq_path_feature(text, freq))
    feature.append(freq_meter_feature(text, freq))
    feature.append(freq_memo_feature(text, freq))
    feature.append(freq_planning_feature(text, freq))
    feature.append(freq_pleased_feature(text, freq))
    feature.append(freq_record_feature(text, freq))
    feature.append(freq_out_feature(text, freq))
    feature.append(freq_semicolon_feature(text, freq))
    feature.append(freq_dollar_feature(text, freq))
    feature.append(freq_sharp_feature(text, freq))
    feature.append(freq_exclamation_feature(text, freq))
    feature.append(freq_para_feature(text, freq))
    feature.append(freq_bracket_feature(text, freq))
    feature.append(freq_and_feature(text, freq))
    feature.append(freq_same_feature(text, freq))
    feature.append(freq_zas_feature(text, freq))
    feature.append(freq_its_feature(text, freq))
    feature.append(freq_because_feature(text, freq))
    feature.append(freq_BibleThump_feature(text, freq))
    feature.append(freq_PogChamp_feature(text, freq))
    feature.append(freq_harrdddd_feature(text, freq))
    feature.append(freq_Kappa_feature(text, freq))
    feature.append(freq_thats_feature(text, freq))
    feature.append(freq_what_feature(text, freq))
    feature.append(freq_she_feature(text, freq))
    feature.append(freq_said_feature(text, freq))
    feature.append(freq_whatss_feature(text, freq))
    feature.append(freq_the_feature(text, freq))
    feature.append(freq_difference_feature(text, freq))
    feature.append(freq_1_feature(text, freq))
    feature.append(freq_star_feature(text, freq))
    feature.append(freq_whether_feature(text, freq))
    feature.append(freq_you_feature(text, freq))
    feature.append(freq_skip_feature(text, freq))
    feature.append(freq_DDD_feature(text, freq))
    feature.append(freq_and_feature(text, freq))
    feature.append(freq_0_feature(text, freq))
    feature.append(freq_lmfao_feature(text, freq))
    feature.append(freq_Keepo_feature(text, freq))
    feature.append(freq_King_feature(text, freq))
    feature.append(freq_Dedede_feature(text, freq))
    feature.append(freq_troll_feature(text, freq))
    feature.append(freq_real_feature(text, freq))
    feature.append(freq_just_feature(text, freq))
    feature.append(freq_do_feature(text, freq))
    feature.append(freq_lblj_feature(text, freq))
    feature.append(freq_for_feature(text, freq))
    feature.append(freq_as_feature(text, freq))
    feature.append(freq_long_feature(text, freq))
    feature.append(freq_can_feature(text, freq))
    feature.append(freq_To_feature(text, freq))
    feature.append(freq_gain_feature(text, freq))
    feature.append(freq_speed_feature(text, freq))
    feature.append(freq_You_feature(text, freq))
    feature.append(freq_mean_feature(text, freq))
    feature.append(freq_this_feature(text, freq))
    feature.append(freq_SBLJ_feature(text, freq))
    feature.append(freq_keep_feature(text, freq))
    feature.append(freq_saying_feature(text, freq))
    feature.append(freq_LBLJ_feature(text, freq))
    feature.append(freq_FailFish_feature(text, freq))
    feature.append(freq_duuuude_feature(text, freq))
    feature.append(freq_LOLOLOLOL_feature(text, freq))
    feature.append(freq_if_feature(text, freq))
    feature.append(freq_I_feature(text, freq))
    feature.append(freq_bj_feature(text, freq))
    feature.append(freq_PedoBear_feature(text, freq))
    feature.append(freq_once_feature(text, freq))
    feature.append(freq_fly_feature(text, freq))
    feature.append(freq_over_feature(text, freq))
    feature.append(freq_hold_feature(text, freq))
    feature.append(freq_up_feature(text, freq))
    feature.append(freq_metroid_feature(text, freq))
    feature.append(freq_funny_feature(text, freq))
    feature.append(freq_Indeed_feature(text, freq))
    feature.append(freq_FuzzyRNG_feature(text, freq))
    feature.append(freq_question_feature(text, freq))
    feature.append(freq_sub_feature(text, freq))
    feature.append(freq_sf5_feature(text, freq))
    feature.append(freq_Thats_feature(text, freq))
    feature.append(freq_legitiment_feature(text, freq))
    feature.append(freq_question_feature(text, freq))
    feature.append(freq_called_feature(text, freq))
    feature.append(freq_clear_feature(text, freq))
    feature.append(freq_wow_feature(text, freq))
    feature.append(freq_so_feature(text, freq))
    feature.append(freq_DansGame_feature(text, freq))
    feature.append(freq_race_feature(text, freq))
    feature.append(freq_right_feature(text, freq))
    feature.append(freq_Now_feature(text, freq))


    # --------- Add your own features here ---------
    # Make sure type is int or float

    return feature 
