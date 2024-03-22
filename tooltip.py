import tkinter as tk

class ToolTip(object):
    """
    ToolTip sınıfı, bir widget üzerinde fare ile gezinildiğinde
    yardımcı bilgiler gösteren bir tooltip penceresi oluşturur.
    """
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        """
        Tooltip penceresini gösterir.
        
        :param tip_text: Tooltip'te gösterilecek metin.
        """
        if self.tip_window or not tip_text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         wraplength=160)
        label.pack(ipadx=1)

    def hide_tip(self):
        """
        Tooltip penceresini gizler.
        """
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()
