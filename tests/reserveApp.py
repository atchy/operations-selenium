# coding: UTF-8

import time
import sys
import os

sys.path.append(os.getcwd())

from base.user import User
from base.operation import Operation as Op

user = User('http://example.selenium.jp/reserveApp/','chrome','jp')

user.close_at_finished = False

operations = [
  Op(
    '宿泊日.年を設定',
    Op.OP_SET_TEXT,
    Op.ELM_BY_ID,
    ('reserve_year', '2020')
  ),
  Op(
    '宿泊日.月を設定',
    Op.OP_SET_TEXT,
    Op.ELM_BY_ID,
    ('reserve_month', '8')
  ),
  Op(
    '宿泊日.日を設定',
    Op.OP_SET_TEXT,
    Op.ELM_BY_ID,
    ('reserve_day', '31')
  ),
  Op(
    '宿泊日.日数を設定',
    Op.OP_SET_TEXT,
    Op.ELM_BY_ID,
    ('reserve_term', '5')
  ),
  Op(
    '人数を設定',
    Op.OP_SET_TEXT,
    Op.ELM_BY_ID,
    ('headcount', '3')
  ),
  Op(
    '名前を入力',
    Op.OP_SET_TEXT,
    Op.ELM_BY_ID,
    ('guestname', 'A山A太郎')
  ),
  Op(
    '次へ',
    Op.OP_CLICK_BTN,
    Op.ELM_BY_ID,
    ('goto_next',)
  ),
  Op(
    '確定',
    Op.OP_CLICK_BTN,
    Op.ELM_BY_ID,
    ('commit',)
  )
]

#user.login(account,password)
user.do_test(operations)



