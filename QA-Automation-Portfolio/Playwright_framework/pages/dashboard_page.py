class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.get_by_placeholder("Search")

    def is_search_box_visible(self):
        return self.search_box.is_visible()