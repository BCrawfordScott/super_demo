import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getCharacters } from '../../store/characters'

const Characters = () => {
    const dispatch = useDispatch();
    const characters = useSelector(state => Object.values(state.characters));
    
    useEffect(async () => {
        dispatch(getCharacters());
    }, [dispatch])

    return (
        <>
            <h1>All the Characters!!!!!</h1>
            <ul>
                {characters?.map(char => {
                    return (
                        <li key={char.id}>{char.name}</li>
                    )
                })}
            </ul>  
        </>
    )
}

export default Characters;
