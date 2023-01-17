import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


class Prereq:
    uname = 'standard_user'
    password = 'secret_sauce'


@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()


def test_login_sukses(setup):
    setup.find_element(By.NAME, 'user-name').send_keys(Prereq.uname)
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys(Prereq.password)
    time.sleep(2)
    setup.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    setup.find_element(By.ID, 'logout_sidebar_link').click()
    time.sleep(3)


def test_login_gagal_username_salah(setup):
    setup.find_element(By.NAME, 'user-name').send_keys("wildan")
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys(Prereq.password)
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username and password do not match any user in this service" == response_message)


def test_login_gagal_username_kosong(setup):
    setup.find_element(By.NAME, 'user-name').send_keys("")
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys(Prereq.password)
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username is required" == response_message)


def test_login_gagal_password_salah(setup):
    setup.find_element(By.NAME, 'user-name').send_keys(Prereq.uname)
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys("wildan")
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username and password do not match any user in this service" == response_message)


def test_login_gagal_password_kosong(setup):
    setup.find_element(By.NAME, 'user-name').send_keys(Prereq.uname)
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys("")
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Password is required" == response_message)


def test_login_gagal_data_kosong(setup):
    setup.find_element(By.NAME, 'user-name').send_keys("")
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys("")
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username is required" == response_message)


def test_login_gagal_data_salah(setup):
    setup.find_element(By.NAME, 'user-name').send_keys("wildan")
    time.sleep(2)
    setup.find_element(By.NAME, 'password').send_keys("wildan")
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)
    response_message = setup.find_element(
        By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert ("Epic sadface: Username and password do not match any user in this service" == response_message)
