from pages.feature_page import FeaturePage

def test_p1_youtube_search_atif_aslam(page):
    feature = FeaturePage(page)
    feature.open('https://www.youtube.com')
    feature.search('atif aslam music')
    feature.submit_search()
    feature.wait_for_results()
    feature.screenshot('result.png')