import sublime
import sublime_plugin
import unicodedata

class Slugify(sublime_plugin.TextCommand):
     def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            region_text = region_text.replace(' ', '-').lower()
            ascii_only = unicodedata.normalize('NFKD', region_text).encode('ascii', 'ignore').decode('utf-8')
            self.view.replace(edit, region, ascii_only)