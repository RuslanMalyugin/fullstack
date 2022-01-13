import React from 'react';
import Header from './Header';
import './Home.css';
import family from './imgs/FreeMan.png'
import Footer from "./Footer";


function Home() {
    return (
        <body>
        <Header/>
        <main className='Main'>
            <div className='Banner'>
                <div className='BannerTop'>
                    Не хватает свободного времени? <br/>
                    25 посещений по физ-культуре никак не набираются? <br/>
                    Не хочешь терять стипендию из-за этого? <br/>
                    Или ты хочешь немного заработать? <br/>
                </div>
                <div className='BannerDown'>
                    Наш сервис - для тебя! <br/>
                    Проходи простую регистрацию и оставляй свой заказ.
                </div>
                <a className='Reg' href='/login'>
                    Зарегистрироваться
                </a>
            </div>
            <div className='PicDesc'>
                    <img src={family} className="family-img" alt="family"/> <br/>
                    Освободи себя от отработок!
            </div>
        </main>
        <Footer/>
        </body>
    );
}

export default Home;