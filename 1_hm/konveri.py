# -*- coding: utf-8 -*-
# initializing empty envelops

necessity_envelop = 0  # NEC, необходимые траты
freedom_envelop = 0    # FFA, финансовая свобода
education_envelop = 0  # EDU, образование
long_term_envelop = 0   # LTSS, резерв и на большие покупки
play_envelop = 0       # PLAY, развлечения
give_envelop = 0       # GIVE, подарки

# initializing percent rate
nec_rate = 0.55
ffa_rate = 0.1
edu_rate = 0.1
ltss_rate = 0.1
play_rate = 0.1
give_rate = 0.05
# initializing expected income, expected necessity and other amounts
expected_income = 1000

# invitation, greetings etc.
print ("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press Ctrl+c to exit script.
\n\n Enter the amount please:""")

# initializing handler for standard input
sum = 0

while (sum < expected_income):
    line = int(input())
    sum += line

    necessity_envelop += line * nec_rate
    freedom_envelop += line * ffa_rate
    education_envelop += line * edu_rate
    long_term_envelop += line * ltss_rate
    play_envelop += line * play_rate
    give_envelop += line * give_rate

    print("\n Enter the amount please:")

# final output
print("At the end we have:\n\
    Necessity Envelop has:                       " + str(int(necessity_envelop)) + "\n\
    Financial Freedom Envelop has:               " + str(int(freedom_envelop)) + "\n\
    Education Envelop                            " + str(int(education_envelop)) + "\n\
    Long Term Saving for Spending Envelop has:   " + str(int(long_term_envelop)) + "\n\
    Play Envelop has:                            " + str(int(play_envelop)) + "\n\
    Give Envelop has:                            " + str(int(give_envelop)) + "\n\
    _______________________________________________________________\n\
\
    Thanks for using our software :)")

input('\n\nНажми Enter чтобы закрыть')
