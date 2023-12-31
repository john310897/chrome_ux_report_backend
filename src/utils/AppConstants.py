labels = {
    "search_container": {
        "url_label": "URL's",
        "placeholder": "Enter URL's separated by line breaks",
        "button_label": "Search"
    },
    "filters": [
        {"label": "Choose FCP Threshold", "name": "fcp", "options": [">500", "<1500"]},
        {"label": "Choose LCP Threshold", "name": "lcp", "options": [">500", "<1500"]}
    ],
    "table_headers": ["Page", "Duration", "FCP", "LCP", "FID", "CLS",'SUM','AVG'],
    "metrix":{'FCP':"first_contentful_paint",
                'FID':"first_input_delay",
                'LCP': "largest_contentful_paint",
                'CLS': "cumulative_layout_shift"}
}