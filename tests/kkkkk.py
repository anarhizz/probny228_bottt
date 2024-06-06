import unittest
from main import start_message
from main import reminder_message
from main import set_reminder_name
from main import send_reminder
from main import handle_all_message
from unittest.mock import MagicMock


class TestStartMessage(unittest.TestCase):
    def test_start_message(self):
        result = start_message("kkkk")
        self.assertEqual(result, "wassup homie,i am reminder bot,enter /reminder")


if __name__ == "__name__":
    unittest.main()

    class TestReminderMessage(unittest.TestCase):
        def test_start_message(self):
          desult = reminder_message("sdjf")



if __name__ == "__name__":
    unittest.main()



class TestSetReminder(unittest.TestCase):
    def test_send_reminder(self):
        chat_id=123
        reminder_name='meeting reminder'
        bot=MagicMock()
        expected_message='time to get reminde "{}"!'.format(reminder_name)
        send_reminder(chat_id, reminder_name,bot)
        bot.send_mesage.assert_called_once_with(chat_id,expected_message)

if __name__ == "__name__":
    unittest.main()



class TestHandleAllMeessage(unittest.TestCase):
    def test_handle_all_message(self):
        chat_id=123
        message=MagicMock()
        message.chat.id=chat_id
        bot=MagicMock()
        expected_response="i dont understand what you're saying . to create a reminder,type /reminder"
        handle_all_message(message,bot)
        bot.send_message.assert_called_once_with(chat_id,expected_response)

if __name__ == "__name__":
    unittest.main()