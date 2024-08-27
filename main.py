from experta import *


print('مرحبا بك في نظامنا الديني \n'
      ' يرجى الأجابة بحرف y أو n في كل سؤال يتم سؤاله')
class الصلاة(Fact):
    pass


class شروط0الصلاة(Fact):
    pass


class اركان0الصلاة(Fact):
    pass

class واجبات0الصلاة(Fact):
    pass

class مبطلات0الصلاة(Fact):
    pass

#######################################################
class الصيام(Fact):
    pass

class شرح0لغة(Fact):
    pass


class شروط0الصيام(Fact):
    pass

class أحكام0الصيام(Fact):
    pass

class مفسدات0الصيام(Fact):
    pass

class مفسدات0قضاءوكفارة(Fact):
    pass

class غيرمفسدات0الصيام(Fact):
    pass

class شرح0مفسدات0قضاءوكفارة(Fact):
    pass

class شرح0مفسدات0قضاء0فقط(Fact):
    pass

class شرح0مفسدات0قضاء0فقط1(Fact):
    pass

class شرح0الصيام(Fact):
    pass
################################################################
class المبيع(Fact):
    pass

class الزكاة(Fact):
    pass

class احكام0المبيع(Fact):
    pass

class شروط0المبيع(Fact):
    pass

class شرح0حكم0المبيع(Fact):
    pass

class شرح0شروط0المبيع(Fact):
    pass

class شرح0انعقاد(Fact):
    pass

####################################################33
class شروط_الزكاة(Fact):
    pass
class انواع_الزكاة(Fact):
    pass
class على_من_نحب_الزكاة(Fact):
    pass
class تمنع_الزكاة(Fact):
    pass
class زكاة_التجارة(Fact):
    pass
class زكاة_الانعام(Fact):
    pass
class زكاة_المال(Fact):
    pass
class زكاة_ما_خرج_من_الارض_مقدار(Fact):
    pass
class زكاة_ما_خرج_من_الارض_نصاب(Fact):
    pass
class زكاة_الذهب_والفضة(Fact):
    pass
class نصاب_الذهب(Fact):
    pass
class  نصاب_الذهب_18(Fact):
    pass
class نصاب_الذهب_24(Fact):
    pass
class نصاب_الذهب_21(Fact):
    pass
class نصاب_الفضة_عيار_99(Fact):
    pass
class نصاب_الفضة(Fact):
    pass
class نصاب_المال(Fact):
    pass

class نصاب_المال_مقدار(Fact):
    pass

class نصاب_المال_قيمة(Fact):
    pass

class زكاة_ما_خرج_من_الارض(Fact):
    pass
##
class زكاة_الابل(Fact):
    pass
class زكاة_الابل_نصاب(Fact):
    pass
class زكاة_الابل_مقدار(Fact):
    pass
#
class زكاة_البقر(Fact):
    pass
class زكاة_البقر_نصاب(Fact):
    pass
class زكاة_البقر_مقدار(Fact):
    pass
#
class زكاة_الغنم(Fact):
    pass
class زكاة_الغنم_نصاب(Fact):
    pass
class زكاة_الغنم_مقدار(Fact):
    pass
class LoanOffer(KnowledgeEngine):

    def validate_response(self):
        while True:
            response = input("الرجاء إدخال إجابة صحيحة (y/n): ")
            if response in ['y', 'n']:
                return response

    def getResponse(self, printableMessage):
        while True:
            response = input(printableMessage)
            if response in ['y', 'n']:
                return response
    def final(self):
        print('\n Thank you for using our system. I hope you found what you were looking for. \n'
              'If you have any further queries, please feel free to run the program again.')
    
    @Rule(NOT(الصلاة(W())))
    def صلاة(self):
        self.declare(الصلاة(input("هل تريد المعرفة حول الصلاة؟")))

    @Rule(الصلاة('value' << W()))
    def صلا(self, value):
        if value == 'y':
            self.declare(شروط0الصلاة(input("هل تريد معرفة شروط الصلاة؟")))
        elif value == 'n':
            self.declare(الصيام(input("هل تريد المعرفة حول الصيام؟")))
        else:
            response = self.validate_response()
            self.declare(الصلاة(response))

    @Rule(شروط0الصلاة('value' << W()))
    def شروط(self, value):
        if value == 'y':
            print(
                '1)'
                'الاسلام \n'
                '2)'
                'العقل \n'
                '3)'
                'التمييز \n'
                '4)'
                'الطهارة من النجاسة \n'
                '5)'
                'الطهارة من الحدث\n'
                '6)'
                'دخول الوقت \n'
                '7)'
                'ستر العورة\n'
                '8)'
                'استقبال القبلة \n'
                '9)'
                'النية\n'


            );
            self.final();
        elif value == 'n':
            self.declare(اركان0الصلاة(input("هل تريد معرفة اركان الصلاة؟")))
        else:
            response = self.validate_response()
            self.declare(شروط0الصلاة(response))

    @Rule(اركان0الصلاة('value' << W()))
    def اركان(self, value):
        if value == 'y':
            print(
                '1)'
                ' القيام مع القدرة \n'
                '2)'
                'تكبير الإحرام\n'
                '3)'
                'قرأة الفاتحة\n'
                ' 4)'
                ' الركوع\n'
                ' 5)'
                'الرفع والإعتدال بعد الركوع\n'
                ' 6)'
                'السجود على سبعة أعضاءالسجود على سبعة أعضاء\n'
                '7)'
                ' الرفع من السجود\n'
                '8)'
                ' الجلسة بين السجدتين\n'
                '9)'
                'الطمأنينة في الأركان\n'
                '10)'
                'الترتيب و الموالاه\n'
                '11)'
                'التشهد الأخير\n'
                ' 12)'
                'الجلوس للتشهد الأخير\n'
                ' 13)'
                'الصلاة على النبي والصلوات الإبراهيمية \n'
                ' 14)'
                'التسليمتان\n'
                  )
            self.final();
        elif value == 'n':
            self.declare(واجبات0الصلاة(input("هل تريد معرفة واجبات الصلاة؟")))
        else:
            response = self.validate_response()
            self.declare(اركان0الصلاة(response))

    @Rule(واجبات0الصلاة('value' << W()))
    def واجبات(self, value):
        if value == 'y':
            print('1) جميع التكبيرات عدا الاحرام\n'
                  '2) قول سمع الله لمن حمده\n'
                  '3) قول ربنا ولك الحمد\n'
                  ' 4) سبحان ربي العظيم فالركوع\n'
                  ' 5) ربي اغفر لي بين السجدتين\n'
                  ' 6) التشهد الأول \n'
                  '7) سبحان ربي الاعلى في السجود\n'
                  '8) الجلوس للتشهد الأول\n')
            self.final();
        elif value == 'n':
            self.declare(مبطلات0الصلاة(input("هل تريد معرفة مبطلات الصلاة؟")))
        else:
            response = self.validate_response()
            self.declare(واجبات0الصلاة(response))

    @Rule(مبطلات0الصلاة('value' << W()))
    def مبطلات(self, value):
        if value == 'y':
            print('1)الكلام العمد مع الذكر والعلم\n'
                  '2) الأكل والشرب\n'
                  '3) الضحك\n'
                  ' 4) انكشاف العورة\n'
                  ' 5) الإنحراف عن القبلة كثير\nا'
                  ' 6) العبث المتوالي \n'
                  '7) إنتقاض الطهارة\n')
            self.final();
        elif value == 'n':
            print('مبطلات')
        else:
            response = self.validate_response()
            self.declare(واجبات0الصلاة(response))

###################################################################################
    @Rule(الصيام('value' << W()))
    def صيام(self, value):
        if value == 'y':
            self.declare(شرح0الصيام(input("هل تريد معرفة شرح الصيام؟")))
        elif value == 'n':
            self.declare(المبيع(input("هل تريد معرفة حول المبيع؟")))
        else:
            response = self.validate_response()
            self.declare(الصيام(response))

    @Rule(شرح0الصيام('value' << W()))
    def شرح(self, value):
        if value == 'y':
            self.declare(شرح0لغة(input("هل تريد معرفة شرح الصيام لغة ؟")))
        elif value == 'n':
            self.declare(شروط0الصيام(input("هل تريد معرفة شروط الصيام؟")))
        else:
            response = self.validate_response()
            self.declare(شرح0الصيام(response))

    @Rule(شرح0لغة('value' << W()))
    def لغة(self, value):
        if value == 'y':
            print('الامساك عن المفطرات يوما كاملا من طلوع الفجر الى غروب الشمس ')
            self.final();
        elif value == 'n':
            print('شرح الصيام اصطلاحا:الامساك عن الشيء ')
            self.final();
        else:
            response = self.validate_response()
            self.declare(شرح0لغة(response))

    @Rule(شروط0الصيام('value' << W()))
    def شرح0ص(self, value):
        if value == 'y':
            print(
                '1)'
                ' الاسلام: فلا يجب عل غير المسلم\n'
                '2)'
                'الصحة: فلا يجب عل مريض\n'
                '3)'
                'العقل: فلا يجب عل مجنون ومغمى علبه\n'
                ' 4)'
                'البلوغ: فلا يجب عل الصغير \n'
                ' 5)'
                'الاقامة: فلا يجب عل مسافر وعليه القصاء\n'
                ' 6)'
                'الطهارة: فلا يجب عل الحائض والنفاس \n'
            )
            self.final();
        elif value == 'n':
            self.declare(أحكام0الصيام(input("هل تريد معرفة أحكام الصيام؟")))
        else:
            response = self.validate_response()
            self.declare(شروط0الصيام(response))

    @Rule(أحكام0الصيام('value' << W()))
    def احكام0(self, value):
        if value == 'y':
            self.declare(مفسدات0الصيام(input("هل تريد معرفة مفسدات الصيام؟")))
        elif value == 'n':
                  self.final();
        else:
            response = self.validate_response()
            self.declare(أحكام0الصيام(response))

    @Rule(مفسدات0الصيام('value' << W()))
    def مفسدات(self, value):
        if value == 'y':
            self.declare(مفسدات0قضاءوكفارة(input("مفسدات قضاء وكفارة و مفسدات قضاء فقط.\nهل تريد معرفة ماهي مفسادات قضاء وكفارة؟")))
        elif value == 'n':
            self.declare(غيرمفسدات0الصيام(input("هل تريد معرفة مالا يفسد الصيام؟")))
        else:
            response = self.validate_response()
            self.declare(مفسدات0الصيام(response))

    @Rule(مفسدات0قضاءوكفارة('value' << W()))
    def مفسدات0(self, value):
        if value == 'y':
            print(
            'الغذاء و الجماع و الشروط '
            )
            self.declare(شرح0مفسدات0قضاءوكفارة(input("هل تريد معرفة شرح هذه المفسدات؟")))
        elif value == 'n':
           print(
            'مفسدات قضاء فقط:'
            'القيء و مما يدخل الجوف')
           self.declare(شرح0مفسدات0قضاء0فقط(input("هل تريد معرفة شرح هذه المفسدات؟")))

        else:
            response = self.validate_response()
            self.declare(مفسدات0قضاءوكفارة(response))

    @Rule(شرح0مفسدات0قضاءوكفارة('value' << W()))
    def مفسدات1(self, value):
        if value == 'y':
            print(
                'الغذاء:ان يتناول الصائم غذاء بدون عذر شرعي\n'
                ' الجماع:مجرد التقاء الختانين تكون عل الذكر والانثى\n'
                ' الشروط:\n'
                'ان يكون مختارا لا مكرها\n'
                ' ان يكون مبيتا للنية فان لم ينوي لاكفرة عليه\n'
                ' ان يكون متعمد فالناسي لا كفارة عليه\n'
                ' الا يكون مريضا\n'
            )
            self.final();
        elif value == 'n':
                  self.final();

        else:
            response = self.validate_response()
            self.declare(شرح0مفسدات0قضاءوكفارة(response))

    @Rule(شرح0مفسدات0قضاء0فقط('value' << W()))
    def مفسدات2(self, value):
        if value == 'y':
            print(
                'القيء:\n'
                'ملاء الفم وذاكر للصوم و اقل من ملاء الفم وناسيا\n'
                ' أما مما يدخل الجوف:\n'
                'طعام او شراب \n'
                'دواء \n'
            )
            self.declare(شرح0مفسدات0قضاء0فقط1(input("هل تريد معرفة شرح هذه المفسدات؟")))
        elif value == 'n':
                  self.final();

        else:
            response = self.validate_response()
            self.declare(شرح0مفسدات0قضاء0فقط(response))

    @Rule(شرح0مفسدات0قضاء0فقط1('value' << W()))
    def مفسدات3(self, value):
        if value == 'y':
            print(
                'بالنسبة للقيء:\n'
                '1)ملاء الفم وذاكر للصوم:اذا تعمد اخراج القيء من جوفه خرج كرها دون تعمد فاعاده الى جوفه عامدا وجب القضاء\n'
                ' 2) اقل من ملاء الفم وناسيا:لم يفسد صيامه \n'
                ' أما مما يدخل الجوف: '
                'طعام او شراب: \n'
                '1)اذا اكل من طعام ماتبقي من اسنانه وكان قدر الحمصة ومافوقها\n '
                '2)كل ماليس غذاء رزا عجين حصاة \n'
                '3)اذا اكل شاكا في طلوع الفجر وكان الفجر طالع v'
                '4)اذا اهمل وهو يتممضض فوص الماء الى جوفه \n'
                'دواء: '
                '1)اذا تناول دواء لعذر شرعي\n '
                '2)اذا داوى جرحا في راسه فوصل الدواء الى جوفه او دمماغه\n'
            )
            self.final();

        elif value == 'n':
                  self.final();

        else:
            response = self.validate_response()
            self.declare(شرح0مفسدات0قضاء0فقط1(response))

    @Rule(غيرمفسدات0الصيام('value' << W()))
    def مفسدات5(self, value):
        if value == 'y':
            print(
               'السواك\n'
               'شم روائح عطرية \n'
               'اذا دخل رمل او غبار الطريق \n'
               'الحجامة \n'
               'المضمضة والاستنشاق شرط عدم الدخول الى الجوف \n'
               'اذا تكون ريقه في فمه فابتلعه عمدا \n'
               'الاغتسال وتبريد الجسم \n'
            )
            self.final();

        elif value == 'n':
                   self.final();

        else:
            response = self.validate_response()
            self.declare(غيرمفسدات0الصيام(response))

        ########################################################################
    @Rule(المبيع('value' << W()))
    def مبيع0(self, value):
        if value == 'y':
            self.declare(احكام0المبيع(input("هل تريد معرفة ماهي أحكام المبيع؟")))
        elif value == 'n':
            self.declare(الزكاة(self.getResponse("هل تريد معرفة حول الزكاة؟")))
        else:
            response = self.validate_response()
            self.declare(المبيع(response))

    @Rule(الزكاة('value' << W()))
    def الزكاة2(self, value):
        if value == 'y':
            self.declare(شروط_الزكاة(self.getResponse("هل تريد معرفة ماهي شروط وجوب الزكاة؟")))
        elif value == 'n':
                  self.final();


    @Rule(شروط_الزكاة('value' << W()))
    def شروط_الزكاة(self, value):
        if value == 'y':
            print(
                'ان لايكون على المال دين\n'
                'ان يكون المال قابلا للنمو\n'
                'الملكية التامة\n '
                'اكتمال الحول وهو سنة هجرية\n'
                'بلوغ النصاب\n'
                'الحرية فلا تجب على العبد\n'
                'الإسلام\n')
            self.final();
        elif value == 'n':
            self.declare(على_من_نحب_الزكاة(self.getResponse("هل تريد معرفة عل من تجب الزكاة؟")))

    @Rule(على_من_نحب_الزكاة('value' << W()))
    def على_من_نحب_الزكاة(self, value):
        if value == 'y':
            print(
               '\n ابن السبيل'
               '\n الخارجون للجهاد'
               '\n الغامرون'
               '\n وفي الرقاب'
               '\n المؤلفة قلوبهم'
               '\n العاملون عليها'
               '\n المساكين'
               '\n الفقراء'
               )
            self.final();
        elif value == 'n':
            self.declare(تمنع_الزكاة(self.getResponse("هل تريد معرفة عل تمنع الزكاة ؟")))
    @Rule(تمنع_الزكاة('value' << W()))
    def  تمنع_الزكاة(self, value):
        if value == 'y':
           print(
               '\n الأولاد '    
               '\n الآباء والأمهات إن علو'    
               '\n الأصول والفروع'
           )
           print('\n Thank you for using our system. I hope you found what you were looking for. \n'
                 'If you have any further queries, please feel free to run the program again.')
        elif value == 'n':
            self.declare(انواع_الزكاة(self.getResponse("هل تريد معرفة انواع الزكاة؟")))

    @Rule(انواع_الزكاة('value' << W()))
    def  انواع_الزكاة(self, value):

        if value == 'y':
            print(
                '\n زكاة التجارة'
                '\nزكاة ماخرج من الأرض '
                '\n زكاة  الذهب والفضة'
                '\n زكاة المال'
                '\n زكاة الأنعام'
            )

            self.declare(زكاة_المال(self.getResponse("هل تريد معرفة عن زكاة المال؟")))
        elif value == 'n':
                 self.final();

    @Rule(زكاة_المال('value' << W()))
    def زكاة_المال(self, value):
        if value == 'y':
            print(
            'نصاب المال '
            )
            self.declare(نصاب_المال(self.getResponse("هل تريد معرفة عن نصاب المال ")))
        elif value == 'n':
            self.declare(زكاة_الذهب_والفضة(self.getResponse("هل تريد معرفة عن زكاة ذهب والفضة")))

    @Rule(نصاب_المال('value' << W()))
    def  نصاب_المال(self, value):
        if value == 'y':
            print(
                '\n قيمة'
                '\n مقدار'
            )
            self.declare(نصاب_المال_قيمة(self.getResponse("هل تريد معرفة عن قيمة نصاب المال ")))
        elif value == 'n':
                 self.final();

    @Rule(نصاب_المال_قيمة('value' << W()))
    def  نصاب_المال_قيمة(self, value):
        if value == 'y':
            print('85g of Gold')
            self.final();
        elif value == 'n':
            self.declare(نصاب_المال_مقدار(self.getResponse("هل تريد معرفة عن مقدار نصاب المال ")))

    @Rule(نصاب_المال_مقدار('value' << W()))
    def  نصاب_المال_مقدار(self, value):
        if value == 'y':
            print('2.5%')
            self.final();
        elif value == 'n':
                   self.final();

    @Rule(زكاة_الذهب_والفضة('value' << W()))
    def زكاة_الذهب_والفضة(self, value):
        if value == 'y':
            print(
                '\n نصاب الذهب'
                '\n نصاب الفضة'
                )
            self.declare(نصاب_الذهب(self.getResponse("هل تريد معرفة عن نصاب ذهب")))
        elif value == 'n':
            self.declare(زكاة_ما_خرج_من_الارض(self.getResponse("هل تريد معرفة عن زكاة ماخرج من الارض")))


    @Rule(نصاب_الذهب('value' << W()))
    def نصاب_الذهب(self, value):
        if value == 'y':
            print(
                '\n عيار18'
                '\n عيار 21 '
                '\n عيار 24 '
                )
            self.declare(نصاب_الذهب_18(self.getResponse("هل تريد معرفة عن نصاب  18")))
        elif value == 'n':
            self.declare(نصاب_الفضة(self.getResponse("هل تريد معرفة عن نصاب الفضة")))

    @Rule(نصاب_الذهب_18('value' << W()))
    def نصاب_الذهب_18(self, value):
        if value == 'y':
            print('113,3غ')
            self.final();
        elif value == 'n':
            self.declare(نصاب_الذهب_21(self.getResponse("هل تريد معرفة عن نصاب  21")))

    @Rule(نصاب_الذهب_21('value' << W()))
    def نصاب_الذهب_21(self, value):
        if value == 'y':
            print('92,1غ')
            self.final();
        elif value == 'n':
            self.declare(نصاب_الذهب_24(self.getResponse("هل تريد معرفة عن نصاب  24")))

    @Rule(نصاب_الذهب_24('value' << W()))
    def نصاب_الذهب_24(self, value):
        if value == 'y':
            print('85غ')
            self.final();
        elif value == 'n':
                 self.final();

    @Rule(نصاب_الفضة('value' << W()))
    def نصاب_الفضة(self, value):
        if value == 'y':
            print('عيار 99.9')
            self.declare(نصاب_الفضة_عيار_99(self.getResponse("هل تريد معرفة عن نصاب فضة 99")))
        elif value == 'n':
                 self.final();

    @Rule(زكاة_ما_خرج_من_الارض('value' << W()))
    def زكاة_ما_خرج_من_الارض(self, value):
        if value == 'y':
            print (
                'نصاب\n'
                'مقدار\n'
            )
            self.declare(زكاة_ما_خرج_من_الارض_نصاب(self.getResponse("هل تريد معرفة عن نصاب  ")))
        elif value == 'n':
            self.declare(زكاة_الانعام(self.getResponse("هل تريد معرفة عن زكاة الانعام  ")))

    @Rule(زكاة_الانعام('value' << W()))
    def زكاة_الانعام(self, value):
        if value == 'y':
            print (
                '\n الإبل'
                '\n البقر'
                '\n الغنم'
            )
            self.declare(زكاة_الابل(self.getResponse("هل تريد معرفة عن الإبل  ")))
        elif value == 'n':
            self.final();

    @Rule(زكاة_الابل('value' << W()))
    def زكاة_الابل(self, value):
        if value == 'y':
            print (
                '\n نصاب'
                '\n مقدار'
            )
            self.declare(زكاة_الابل_نصاب(self.getResponse("هل تريد معرفة عن نصاب  ")))
        elif value == 'n':
            self.declare(زكاة_البقر(self.getResponse("هل تريد معرفة عن زكاة البقر  ")))

    @Rule(زكاة_الابل_نصاب('value' << W()))
    def زكاة_الابل_نصاب(self, value):
        if value == 'y':
            print (
                '5'
            )
            self.final()
        elif value == 'n':
            self.declare(زكاة_الابل_مقدار(self.getResponse("هل تريد معرفة عن مقدار  ")))

    @Rule(زكاة_الابل_مقدار('value' << W()))
    def زكاة_الابل_مقدار(self, value):
        if value == 'y':
            print (
                'من 5 شاة واحدة'
            )
            self.final()
        elif value == 'n':
            self.final()

    @Rule(زكاة_البقر('value' << W()))
    def زكاة_البقر(self, value):
        if value == 'y':
            print (
                '\n نصاب'
                '\n مقدار'
            )
            self.declare(زكاة_البقر_نصاب(self.getResponse("هل تريد معرفة عن نصاب  ")))
        elif value == 'n':
            self.declare(زكاة_الغنم(self.getResponse("هل تريد معرفة عن زكاة الغنم  ")))

    @Rule(زكاة_البقر_نصاب('value' << W()))
    def زكاة_البقر_نصاب(self, value):
        if value == 'y':
            print (
                '30'
            )
            self.final()
        elif value == 'n':
            self.declare(زكاة_البقر_مقدار(self.getResponse("هل تريد معرفة عن مقدار  ")))

    @Rule(زكاة_البقر_مقدار('value' << W()))
    def زكاة_البقر_مقدار(self, value):
        if value == 'y':
            print (
                'من 30 بقرة واحدة'
            )
            self.final()
        elif value == 'n':
            self.final()

    @Rule(زكاة_الغنم('value' << W()))
    def زكاة_الغنم(self, value):
        if value == 'y':
            print (
                '\n نصاب'
                '\n مقدار'
            )
            self.declare(زكاة_الغنم_نصاب(self.getResponse("هل تريد معرفة عن نصاب  ")))
        elif value == 'n':
            self.final()

    @Rule(زكاة_الغنم_نصاب('value' << W()))
    def زكاة_الغنم_نصاب(self, value):
        if value == 'y':
            print (
                '40'
            )
            self.final()
        elif value == 'n':
            self.declare(زكاة_الغنم_مقدار(self.getResponse("هل تريد معرفة عن مقدار  ")))

    @Rule(زكاة_الغنم_مقدار('value' << W()))
    def زكاة_الغنم_مقدار(self, value):
        if value == 'y':
            print (
                '40-120 واحدة'
            )
            self.final()
        elif value == 'n':
            self.final()


    @Rule(زكاة_ما_خرج_من_الارض_نصاب('value' << W()))
    def زكاة_ما_خرج_من_الارض_نصاب(self, value):
        if value == 'y':
            print('612kg من القمح و نحوه')
            self.final();
        elif value == 'n':
            self.declare(زكاة_ما_خرج_من_الارض_مقدار(self.getResponse("هل تريد معرفة عن مقدار  ")))

    @Rule(زكاة_ما_خرج_من_الارض_مقدار('value' << W()))
    def زكاة_ما_خرج_من_الارض_مقدار(self, value):
        if value == 'y':
            print (
                '\n نصف العشر بالري'
                '\n العشر لمن سقي بماء المطر'
            )
            self.final();
        elif value == 'n':
                 self.final();

    @Rule(نصاب_الفضة_عيار_99('value' << W()))
    def نصاب_الفضة_عيار_99(self, value):
        if value == 'y':
            print('595غ')
            self.final();
        elif value == 'n':
                 self.final();

    @Rule(احكام0المبيع('value' << W()))
    def حكم0مبيع(self, value):
        if value == 'y':
          print(
              '1)بيوع منهي عنها\n'
              '2)بيوع مباحة')
          self.declare(شرح0حكم0المبيع(input("هل تريد معرفة شرح هذه الاحكام؟")))

        elif value == 'n':
            self.declare(شروط0المبيع(input("هل تريد معرفة ماهي شروط المبيع؟")))
        else:
            response = self.validate_response()
            self.declare(احكام0المبيع(response))

    @Rule(شروط0المبيع('value' << W()))
    def شرط0مبيع(self, value):
        if value == 'y':
            print(
               '1)انعقاد \n'
               '2)صحة \n'
               '3)نفاذ \n'
               '4)لزوم \n'
            )
            self.declare(شرح0شروط0المبيع(input("هل تريد معرفة شرح هذه شروط؟")))
        elif value == 'n':
                  self.final();
        else:
            response = self.validate_response()
            self.declare(شروط0المبيع(response))

    @Rule(شرح0حكم0المبيع('value' << W()))
    def شرح0حكم(self, value):
        if value == 'y':
            print(

                '1)بيوع منهي عنها:\n'
                'بيع الثنيا\n '
                'تلقي الركبان \n'
                'بيع الملامسة \n'
                'بيع الحصاة \n'
                'بيع الغرر \n'
                'بيع الغش \n'
                'بيع المحتكر \n'
                'العِينةِ \n'
                '\n'
                '2)بيوع مباحة: \n'
                'اقالة \n'
                'عقد مرابحة\n'
            )
            self.final();



        elif value == 'n':
            self.final();
        else:
            response = self.validate_response()
            self.declare(شرح0حكم0المبيع(response))

    @Rule(شرح0شروط0المبيع('value' << W()))
    def شرح0شروط(self, value):
        if value == 'y':
            print(
                '1)انعقاد:\n'
                'متعلقة بالعاقدين '
                'متعلقة بالمعقود عليه '
                'متعلقة بالصيغة \n'
                '2)صحة:\n'
                'انتفاء الجهالة '
                'عدم الغرر '
                'عدم الضرر '
                'انتفاء الاكراه '
                'عدم التوقيت '
                'عدم وجود شرط مفسد '
                '\n '
                '3)نفاذ:\n '
                'الملك والولاية'
                ' ألا يكون في مبيع حق لغير البائع '
                '4)لزوم '
            )
            self.declare(شرح0انعقاد(input("هل تريد معرفة شرح مزيد حول انعقاد؟")))

        elif value == 'n':
            print('not')
        else:
            response = self.validate_response()
            self.declare(شرح0شروط0المبيع(response))

    @Rule(شرح0انعقاد('value' << W()))
    def شرح1شروط(self, value):
        if value == 'y':
            print(

                '1)متعلقة بالعاقدين:\n '
                ' أهلا للتصرف '
                'الولاية عل عقد '
                'حرية الاختيار '
                '2)متعلقة بالمعقود عليه \n'
                'موجوداً '
                'قدرة على تسليمه '
                'يباح الانتفاع به '
                'معلوماً للمتعاقدين '
                'ملكاً للبائع '
                'خاليا من موانع الصحة '
                
                '3)متعلقة بالصيغة \n'
                'في مجلس واحد '
                'قبول موافقاً للإجاب '
                'بلفظ الماضي والمضارع  '

            )


        elif value == 'n':
                  self.final();
        else:
            response = self.validate_response()
            self.declare(شرح0انعقاد(response))





offer = LoanOffer()
offer.reset()
offer.run()
