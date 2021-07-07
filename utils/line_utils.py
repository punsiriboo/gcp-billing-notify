from line_notify import LineNotify

class LineUtils:
    
    
    def __init__(self, token):
        self.ACCESS_TOKEN=token
    
    def send_line(self, message, recipient):
        notify = LineNotify(self.ACCESS_TOKEN)
        notify.send(message)