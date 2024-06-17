from pydantic import BaseModel


class GithubSearchModel(BaseModel):
    keyword_search_url: str = "https://api.github.com/search/repositories?q="
    topic_search_url: str = "https://api.github.com/search/repositories?q=topic:{topic}+is:featured"
    github_base_url: str = "https://github.com"

    def keyword_url(self, keyword: str) -> str:
        return self.keyword_search_url + keyword

    def topic_url(self, topic: str) -> str:
        return self.topic_search_url.format(topic=topic)
