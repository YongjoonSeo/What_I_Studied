```python
# 1. access key 붙여넣기
    client_id = 'OYiUavoFiP3Pw_RTEk7BVpu6hOoUWr2TCl5l1S3iwe0'
    # 2. form 데이터 가져오기(설정한 name 속성값 -> search)
    search_data = request.GET.get('search')
    # 3. api 요청 보내기 (이 api를 사용하기 위해 access_key랑 어떤 데이터를 검색할지 두 개를 보내줘야 한다. (필수인자는 query 하나))
    photo_url = f'https://api.unsplash.com/search/photos?query={search_data}&client_id={client_id}'
    response = requests.get(photo_url).json()
    # https://api.unsplash.com/search/photos?query=cat&client_id=OYiUavoFiP3Pw_RTEk7BVpu6hOoUWr2TCl5l1S3iwe0
    photo_list = []
    for photo in response.get('results'):
        photo_list.append(photo.get('urls').get('regular'))
    context = {
        'photo_list': photo_list
    }
```

