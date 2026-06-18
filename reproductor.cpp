#define MINIAUDIO_IMPLEMENTATION
#include "miniaudio.h"
#include <iostream>
#include <thread>
#include <chrono>
int main(int argc,char** argv){
    if(argc<2) {
        std::cerr<<"Burro, se usa asi ./reproductor <ruta_de_tu_cancion>, imbecil!"<<std::endl;
        return -1;;
    }
    ma_engine motor;
    if (ma_engine_init(NULL,&motor)!=MA_SUCCESS){
        std::cerr<<"Tarado no se inicializo el motor, resuelvelo o tu tarjeta de audio es una porqueria"<<std::endl;
        return -1;
    }
    ma_sound sound;
    if (ma_sound_init_from_file(&motor, argv[1], 0, NULL,NULL,&sound)!=MA_SUCCESS){
        std::cerr<<"No hay musica papi, pon una ruta valida"<<std::endl;
        ma_engine_uninit(&motor);
        return -1;
    }
    //std::cout<<"Ahi va la cancion cholo..."<<std::endl;
    ma_sound_start(&sound);
    while (ma_sound_is_playing(&sound)) {
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    //std::cout<<"Se acabo cholo"<<std::endl;
    ma_sound_uninit(&sound);
    ma_engine_uninit(&motor);
    return 0;
}
