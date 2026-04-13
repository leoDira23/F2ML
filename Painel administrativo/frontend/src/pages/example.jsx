
import React, { useState } from 'react';

const App = () => {
  // 1. Criamos um estado para saber qual card mostrar (começa com o card 1)
  const [activeTab, setActiveTab] = useState(1);

  // Lista de cards para facilitar a renderização (opcional, mas recomendado)
  const cards = [
    { id: 1, title: "Card Um", content: "Conteúdo do primeiro card." },
    { id: 2, title: "Card Dois", content: "Conteúdo do segundo card." },
    { id: 3, title: "Card Três", content: "Conteúdo do terceiro card." },
    { id: 4, title: "Card Quatro", content: "Conteúdo do quarto card." },
    { id: 5, title: "Card Cinco", content: "Conteúdo do quinto card." },
  ];

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      {/* 2. Navbar com botões que alteram o estado */}
      <nav style={{ marginBottom: '20px', display: 'flex', gap: '10px' }}>
        {cards.map((card) => (
          <button 
            key={card.id}
            onClick={() => setActiveTab(card.id)}
            style={{
              padding: '10px',
              backgroundColor: activeTab === card.id ? '#007bff' : '#f0f0f0',
              color: activeTab === card.id ? 'white' : 'black',
              cursor: 'pointer',
              border: 'none',
              borderRadius: '5px'
            }}
          >
            Ver Card {card.id}
          </button>
        ))}
      </nav>

      {/* 3. Lógica de exibição: Só mostra o card se o ID bater com o activeTab */}
      <div className="card-container">
        {cards.map((card) => (
          activeTab === card.id && (
            <div key={card.id} style={{ border: '1px solid #ccc', padding: '20px', borderRadius: '8px' }}>
              <h2>{card.title}</h2>
              <p>{card.content}</p>
            </div>
          )
        ))}
      </div>
    </div>
  );
};

export default App;

