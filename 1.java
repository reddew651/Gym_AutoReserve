// ==UserScript==
// @name         Gym Auto Click
// @namespace    http://tampermonkey.net/
// @version      2025-03-13
// @description  Auto click elements using XPath
// @author       Reddew
// @match        https://gym.sysu.edu.cn/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const COMMON_XPATHS = [
        '//*[@id="app"]/div/div[2]/main/section[1]/div/div[4]/h3',
        '//*[@id="app"]/div/div[2]/main/div[4]/div[4]',
        '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[3]/div[3]'
    ];

    const FINAL_CONFIRM = '//*[@id="app"]/div/div[2]/div[3]/div/button';

    const TIME_SLOTS = {
        FIRST: '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[2]/button',
        SECOND: '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[2]/td[2]/button',
        THIRD: '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[3]/td[2]/button',
        FOURTH: '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[4]/table/tbody/tr[4]/td[2]/button'
    };

    function getTimeSlotXPath() {
        const today = new Date().getDay(); // 0 是周日，1-6 是周一到周六
        
        if (today === 1 || today === 6) {
            return TIME_SLOTS.FOURTH;
        }
        else if ([2, 5].includes(today)) {
            return TIME_SLOTS.THIRD;
        }
        else if ([3].includes(today)) {
            return TIME_SLOTS.FIRST;
        }
        return null;
    }

    async function clickElement(xpath) {
        const element = document.evaluate(xpath, document, null, 
            XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (!element) return false;
        
        try {
            element.click();
            return true;
        } catch (error) {
            return false;
        }
    }

    async function processClicks(index = 0) {
        const timeSlotXPath = getTimeSlotXPath();
        if (!timeSlotXPath) {
            console.log('Today is not a valid day for booking');
            return;
        }

        const XPATHS = [...COMMON_XPATHS, timeSlotXPath, FINAL_CONFIRM];
        
        if (index >= XPATHS.length) return;

        if (await clickElement(XPATHS[index])) {
            console.log(`Successfully clicked: ${XPATHS[index]}`);
            setTimeout(() => processClicks(index + 1), 500);
        } else {
            console.log(`Failed to click: ${XPATHS[index]}, retrying...`);
            setTimeout(() => processClicks(index), 1000);
        }
    }

    // 页面加载完成后开始执行
    window.addEventListener('load', () => setTimeout(processClicks, 2000));
})();