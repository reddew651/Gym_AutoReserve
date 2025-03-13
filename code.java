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

    const XPATHS = [
        '//*[@id="app"]/div/div[2]/main/section[1]/div/div[4]/h3',
        '//*[@id="app"]/div/div[2]/main/div[4]/div[4]',
        '//*[@id="app"]/div/div[2]/main/div/div[2]/div[1]/div[3]/div[3]'
    ];

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
        if (index >= XPATHS.length) return;

        if (await clickElement(XPATHS[index])) {
            setTimeout(() => processClicks(index + 1), 500);
        } else {
            setTimeout(() => processClicks(index), 1000);
        }
    }

    // 页面加载完成后开始执行
    window.addEventListener('load', () => setTimeout(processClicks, 2000));
})();