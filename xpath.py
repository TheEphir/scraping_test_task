def get_brain_com_ua_xpath():
    return {
    "full_name":'//div[@class="title"]/h1',
    "color":'//a[contains(@title, "Колір")]',
    "storage":'//a[contains(@title, "Вбудована пам")]',
    "seller":'//div[@class="logo"]/a',
    "price":'//div[@class="br-pr-np"]/div/span',
    "discount_price":'//span[@class="red-price"]',
    "photos":'//div[contains(@class, "slick-slide slick")]/img',
    "item_id":'//div[@class="container br-container-main br-container-prt"][contains(data-code,"")]',
    "review_count":'//div[@class="br-pt-rt-main-mark"]//a[@href="#reviews-list"]/span',
    "series":'//div[@class="container br-container-main br-container-prt"][contains(data-model,"")]',
    "screen":'//a[contains(@title, "Діагональ")]',
    "resolution":'//a[contains(@title, "Роздільна здатність екрану")]',
    "all_specs":'//div[@class="br-pr-chr-item"]/div/div',
}