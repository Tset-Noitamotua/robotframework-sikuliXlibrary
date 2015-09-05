*** Settings ***
Documentation
...  The purpose of this test suite is to test the functionality of
...  'Robot Framework SikuliXLibrary'.
...
...  Start testexecution:
...    in CMD:
...      jybottest library_self_test.robot
...      NOTE: this will run all tests in this suite.
...
...    in CMD with options:
...      jybottest --include TAG_1 --noncritical TAG_2 library_self_test.robot
...      NOTE: this will only run tests with TAG_1 AND additionally test with
...      TAG_2 will be treated as noncritical and thus will have no influence
...      on overall suite result.
...    from file explorer:
...      doubleclick run_library_self_test_with_jybot.bat OR ~...pybot.bat
...
Library  SikuliXLibrary  library_self_test_images
...                      greeting='Bring back hairy pussies, man!!!'
...                      timeout=5.55  similarity=0.77
Test Setup  Start Calculator and Focus it's window



*** Variables ***
${error_msg}    Don't f**k with bad errors!



*** Test Cases ***
SikuliXLibrary Arguments
    [Tags]      log
    # [Setup]  NONE
    log library arguments


# ----------------------------------------------------------------------------
# 1.  ALL TESTS WITH OCR OFF
# ----------------------------------------------------------------------------
#     NOTE: SikuliX's OCR function is turned off during test run.

# ----------------------------------------------------------------------------
# 1.1 CLICK SHOULD PASS ------------------------------------------------------

Click Image
    [Tags]      click
    click       btnC.png

Click Image + simple post condition check
    [Tags]      click
    click       btn2.png    CalcApp.png

Click Image + enhanced post conditions check
    [Tags]      click
    click       btnC.png    CalcApp.png     similarity=0.66
    click       btn2.png    CalcApp.png     similarity=0.77     timeout=0.33
    click       btnC.png    CalcApp.png     timeout=0.44
    click       btn2.png    CalcApp.png     timeout=0.55        similarity=0.88

Click Location (location=value,value)
    [Tags]      click
    click       location=0,0
    click       location=0,1
    click       location=100,101
    click       location=111, 112
    # TODO:     Make Location click with simple and enhanced post_ocnd. checks!

Click Location (xy=value,value)
    [Tags]      click
    click       xy=0,0
    click       xy=333,334
    click       xy=444, 445
    # TODO:     Make Location click with simple and enhanced post_ocnd. checks!

Click Location (x=value y=value)
    [Tags]      click
    click       x=0     y=0
    click       x=222   y=223
    # TODO:     Make Location click with simple and enhanced post_ocnd. checks!

Click Elements in Sequence
    [Tags]      click
    click       btnPlus.png
    click       btn2.png
    click       btnEqual.png


# 1.2 CLICK SHOULD FAIL ------------------------------------------------------
# ----------------------------------------------------------------------------

Click Should Fail - ERROR(1): NO args or kwargs passed
    [Tags]            click
    ${error_msg}      Run Keyword And Expect Error    *     click
    Should Start With   ${error_msg}        AttributeError: NO (kw)args passed!

Click Should Fail - ERROR(2): TOO many arguments passed
    [Tags]            click
    ${error_msg_1}    Run Keyword And Expect Error    *    click   image1  image2  image3
    ${error_msg_2}    Run Keyword And Expect Error    *    click   btnC.png    CalcApp.png   btn2.png
    Should Start With   ${error_msg_1}      AttributeError: Too many args passed! Max 2 allowed!
    Should Start With   ${error_msg_2}      AttributeError: Too many args passed! Max 2 allowed!

Click Should Fail - ERROR(3): Invalid argument(s) passed
    [Tags]              click
    ${error_msg_1}      Run Keyword And Expect Error    *   click   image
    ${error_msg_2}      Run Keyword And Expect Error    *   click   image1  image2
    Should Start With   ${error_msg_1}      AttributeError: Invalid argument passed! Should end with .png
    Should Start With   ${error_msg_2}      AttributeError: Invalid argument passed! Should end with .png

    ${error_msg_1}=         Run Keyword And Expect Error    *   click   location="200,300"
    ${error_msg_2}=         Run Keyword And Expect Error    *   click   x=100
    ${error_msg_3}=         Run Keyword And Expect Error    *   click   location=100,
    ${error_msg_4}=         Run Keyword And Expect Error    *   click   location=100
    ${error_msg_5}=         Run Keyword And Expect Error    *   click   location=0.1
    ${error_msg_6}=         Run Keyword And Expect Error    *   click   x=100
    ${error_msg_7}=         Run Keyword And Expect Error    *   click   similarity=0.5

    Should Start With       ${error_msg_1}      ValueError: invalid literal for int()
    Should Start With       ${error_msg_2}      AttributeError: FUCK INVALID ARGUMENTS!
    Should Start With       ${error_msg_3}      ValueError: invalid literal for int()
    Should Start With       ${error_msg_4}      IndexError: index out of range:
    Should Start With       ${error_msg_5}      ValueError: invalid literal for int()
    Should Start With       ${error_msg_6}      AttributeError: FUCK INVALID ARGUMENTS!
    Should Start With       ${error_msg_7}      AttributeError: FUCK INVALID ARGUMENTS!

Click Should Fail - ERROR(4): NO Reference Image File or Can't Be Loaded
    [Tags]              click   error
    [Documentation]     Trys to click element which has NO Reference image file.
    Run Keyword And Expect Error    FindFailed: Region: doFind: Image not loadable: image.png   click   image.png

Click Should Fail - ERROR(5): Element NOT available or not visible
    [Tags]              click   error   new
    [Documentation]     Trys to click an Element which is not available during test run.
    ${error_msg_1}      Run Keyword And Expect Error    *   click       btnExp.png
    Should Start With       ${error_msg_1}      FindFailed: can not find btnExp.png in R

In Region Click Should Fail - ERROR: Element NOT available or not visible
    [Tags]              in_region   click   new
    set region          CalcApp.png
    ${error_msg_1}      Run Keyword And Expect Error    *   click       btnExp.png
    Should Start With   ${error_msg_1}          FindFailed: can not find btnExp.png in R


# ----------------------------------------------------------------------------
# 1.3 RIGHT CLICK SHOULD PASS ------------------------------------------------
##    TODO: NOTE: Right Click Tests do not workk properly yet!
##    TODO: Need to check them in detail, there are some 'Region' related issues!

# Right Click Image
#     [Tags]          right_click     new
#     right click     calc_display.png
#     # makes a click to close contextmenu and get back to default state
#     click           btnC.png
#
# Right Click Image + simple post condition check
#     [Tags]          right_click     new
#     right click     calc_display.png    calc_display_contextmenu.png
#     # makes a click to close contextmenu and get back to default state
#     click           btnC.png
#
# Right Click Image + enhanced post conditions check
#     [Tags]          right_click     new
#     right click     calc_display.png    calc_display_contextmenu.png    similarity=0.5
#     # makes a click to close contextmenu and get back to default state
#     click           btn2.png
#     right click     calc_display.png    calc_display_contextmenu.png    similarity=0.57    timeout=0.33
#     # makes a click to close contextmenu and get back to default state
#     click           btn2.png
#     right click     calc_display.png    calc_display_contextmenu.png    timeout=0.44    similarity=0.66
#     # makes a click to close contextmenu and get back to default state
#     click           btn2.png
#
# Right Click Location_1
#     [Tags]          right_click
#     Fail
#
# Right Click Location_2
#     [Tags]          right_click
#     Fail
#
# Right Click Location_3
#     [Tags]          right_click
#     Fail
#
# In Region Right Click
#     [Tags]          in_region   right_click   new
#     set region      CalcApp.png
#     right click     btn2.png
#
# # -------------------------------------------------------------------------------------------------
# # 1.4 RIGHT CLICK SHOULD FAIL
#
# Right Click Should Fail - ERROR: Element NOT available or not visible
#     [Tags]      right_click   error     new
#     ${error_msg}    Run Keyword And Expect Error    *   right click    btnExp.png
#     Should Start With   ${error_msg}   FindFailed: can not find btnExp.png in R
#
# In Region Right Click Should Fail - ERROR: Element NOT available or not visible
#     [Tags]          in_region   error   right_click   new
#     set region      CalcApp.png
#     ${error_msg}    Run Keyword And Expect Error    *   right click    btnExp.png
#     Should Start With   ${error_msg}   FindFailed: can not find btnExp.png in R



# ----------------------------------------------------------------------------
# 2.  ALL TESTS WITH OCR ON
# ----------------------------------------------------------------------------
#     NOTE: SikuliX's OCR function is turned on during test run
#     TODO: NOTE: OCR ON ends where the keyword 'switch ocr   OFF' is used
#     TODO:       first time - see below!!!
#     TODO: delete this NOTE and 'switch orc' keywords when OCR ready!!!

# ----------------------------------------------------------------------------
# 2.1 CLICK SHOULD PASS ------------------------------------------------------

Click Image (OCR ON)
    [Tags]      click       ocr_on
    # TODO: NOTE: for now just simulating OCR ON/OFF by keyword 'switch ocr'
    # TODO: Delete it after OCR ready!
    switch ocr  ON

    click       btnC.png

Click Image + simple post condition check (OCR ON)
    [Tags]      click       ocr_on
    click       btn2.png    CalcApp.png

Click Image + enhanced post conditions check (OCR ON)
    [Tags]      click
    click       btnC.png    CalcApp.png     similarity=0.66
    click       btn2.png    CalcApp.png     similarity=0.77     timeout=0.33
    click       btnC.png    CalcApp.png     timeout=0.44
    click       btn2.png    CalcApp.png     timeout=0.55        similarity=0.88

Click Text (OCR ON)
    [Tags]      click   ocr_on
    click       image

Click Text + simple post condition check (OCR ON)
    [Tags]      click   ocr_on
    # TODO:     Make post cond. available for 'Click (by Text)'
    click       image1  image2

Click Text + enhanced post conditions check (OCR ON)
    [Tags]      click   ocr_on
    # TODO
    click       image1  image2   similarity=0.77    timeout=0.55

Click Elements in sequence (OCR ON)
    [Tags]      click   ocr_on
    click       btnPlus.png
    click       btn2.png
    click       btnEqual.png

# ----------------------------------------------------------------------------
# 2.2. CLICK SHOULD FAIL -----------------------------------------------------

Click Should Fail - ERROR(1): NO args or kwargs passed (OCR ON)
    [Tags]      click   error   ocr_on
    Run Keyword And Expect Error    AttributeError: NO (kw)args passed! But at least one arg or kwarg required!     click

Click Should Fail - ERROR(2): TOO many arguments passed (OCR ON)
    [Tags]      click   error   ocr_on
    Run Keyword And Expect Error    AttributeError: Too many args passed! Max 2 allowed!    click   image1  image2  image3
    Run Keyword And Expect Error    AttributeError: Too many args passed! Max 2 allowed!    click   btnC.png    CalcApp.png   btn2.png

Click Should Fail - ERROR(3): Invalid argument(s) passed (OCR ON)
    [Tags]      click   error   ocr_on
    [Documentation]     Trying to click a target with non existing reference image file
    ${error_msg_1}       Run Keyword And Expect Error    *   click   image.png
    Should Start with   ${error_msg_1}      FindFailed: Region: doFind: Image not loadable: image.png

    Run Keyword And Expect Error    *   click   similarity=0.5


Click Should Fail - ERROR(4): Element NOT available or not visible (OCR ON)
    [Tags]      click   error   ocr_on    new

    ${error_msg_1}  Run Keyword And Expect Error    *   click       btnExp.png
    Should Start With   ${error_msg_1}  FindFailed: can not find btnExp.png in R

    # TODO: NOTE: for now just simulating OCR ON/OFF by keyword 'switch ocr'
    # TODO: Delete it after OCR ready
    switch ocr      OFF



# ----------------------------------------------------------------------------
# 3.  BASIC TESTS
# ----------------------------------------------------------------------------
#     TODO: Give them better / meaningfull names!!!


Basic Test 2
    [Tags]          basic
    call keyword

#Basic Test 3
#    [Tags]      basic   mustfail
#    [Documentation]     Passing arguments.
#    [Documentation]     Keyword should fail because no argument is passed but first arg is obligatory.
#    # TODO: Frage an die RF Mailingliste stellen, warum das hier nicht funktioniert!!!
#    Run Keyword And Expect Error     *      pass arguments

Basic Test 4
    [Tags]      basic
    [Documentation]     Passing arguments.
    ...                 Second argument´s default value is 'second argument'
    pass arguments      1. argument

Basic Test 5
    [Tags]      basic
    [Documentation]     Passing arguments.
    ...                 Overwriting second´s argument default value. Now should be '2. NEW'
    pass arguments      1. argument     2. NEW

Basic Test 6
    [Tags]      basic
    [Documentation]     Passing *args.
    pass args
    pass args       zero
    pass args       zero     one
    pass args       zero     one     two
    pass args       1        2.0     3.3
    pass args       \n
    pass args       \t

Basic Test 7
    [Tags]      basic
    [Documentation]     Passing **kwargs.
    pass kwargs
    pass kwargs     first=zero
    pass kwargs     first=zero   second=one
    pass kwargs     first=zero   second=one   third=2.0
    pass kwargs     firtst=\n    2.=second
    pass kwargs     1.=first     2.=\n2.0

Basic Test 8
    [Tags]      basic
    [Documentation]     Passing *args and **kwargs.
    pass args kwargs
    pass args kwargs    one   two   three=3.0

Basic Test 9
    [Tags]      basic
    multiply by two     3

Basic Test 10
    [Tags]      basic
    ${error_msg_1}  Run Keyword And Expect Error    *   multiply by two     three
    Should Start With   ${error_msg_1}      ValueError: invalid literal for

Basic Test 11
    [Tags]      basic
    numbers should be equal     2       2

Basic Test 12
    [Tags]      basic    # TODO Fehlermeldung eintragen
    Run Keyword And Expect Error    *   numbers should be equal     2       3

Basic Test 13
    [Tags]      basic    # TODO Fehlermeldung eintragen
    Run Keyword And Expect Error    *   numbers should be equal     one     two

Calc Test 1
    [Tags]      calc
    # start app
    # verify app
    Verify that 2 plus 2 = 4

Calc Test 2
    [Tags]      calc
    #start app
    #verify app
    Run Keyword And Expect Error    *   Verify that 2 plus 2 = 5

Calc Test 3
    [Tags]      calc
    #start app
    #verify app
    Run Keyword And Expect Error    *   Click on non-existent button 'Exp'

User Action Test 1
    [Tags]      u_act
    start app
    verify app
    click       btnC.png
    click       btn2.png
    click       btnPlus.png
    click       btn2.png
    click       btnEqual.png
    verify result   4

Use Keyboard Shortcut ALT + F4
    [Tags]            shortcut
    [Documentation]   Simulates keyboard shortcut ALT + F4 to close calculator window.
    start app
    verify app
    use keyboard shortcut  \ue022  \ue014           # ALT + F4

Wait Vanish
    [Tags]      shortcut
    start app
    verify app
    use keyboard shortcut  \ue022  \ue014           # ALT + F4 shortcut closes calculator window
    wait vanish     CalcApp.png     timeout=7.7

Wait Vanish Should Fail
    [Tags]      shortcut
    start app
    verify app
    #                                               # Here we don't close calculator, so Wait Vanish must fail
    Run Keyword And Expect Error    *   wait vanish     CalcApp.png     timeout=5.5



*** Keywords ***
Start Calculator and Focus it's window
    start app
    verify app
    click           btnC.png

Verify that 2 plus 2 = 4
    perform action  2  +  2
    verify result   4

Verify that 2 plus 2 = 5
    perform action  2  +  2
    verify result   5

Click on non-existent button 'Exp'
   perform action   2  exp  2
   verify result    2

