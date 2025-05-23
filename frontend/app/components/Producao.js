"use client";

import { useEffect, useState } from "react";

export default function Producao() {
  const [ano, setAno] = useState(2020);
  const [dados, setDados] = useState(null);
  const [loading, setLoading] = useState(false);
  const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000';

  useEffect(() => {
    if (ano < 1900 || ano > 2100) return;
    setLoading(true);
    fetch(`${apiUrl}/api/producao?ano=${ano}`)
      .then(res => res.json())
      .then(data => {
        setDados(data.dados);
        setLoading(false);
      })
      .catch(err => {
        console.error("Erro ao buscar dados:", err);
        setLoading(false);
      });
  }, [ano]);

  const formatNumber = (n) => n?.toLocaleString("pt-BR") ?? "-";

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-100 to-white py-12 px-6">
      <div className="max-w-4xl mx-auto bg-white rounded-2xl shadow-xl p-8">
        <h1 className="text-3xl font-bold text-purple-700 mb-6 text-center">
          Consulta de Produção Vitivinícola
        </h1>

        <div className="mb-8 text-center">
          <label htmlFor="ano" className="block text-lg font-medium text-gray-700 mb-2">
            Digite o ano:
          </label>
          <input
            id="ano"
            name="ano"
            type="number"
            value={ano}
            onChange={(e) => setAno(Number(e.target.value))}
            min="1900"
            max="2100"
            className="border border-gray-300 rounded-lg p-2 text-center w-40 shadow-md focus:ring-purple-500 focus:border-purple-500"
          />
        </div>

        {loading && <p className="text-center text-gray-500">Carregando dados...</p>}

        {Array.isArray(dados) && (
          <div className="space-y-6">
            {dados.map((item, idx) => (
              <div
                key={idx}
                className="border border-purple-300 bg-purple-50 p-4 rounded-xl shadow-sm hover:shadow-md transition-shadow"
              >
                <h2 className="text-xl font-semibold text-purple-800 mb-2">
                  {item.produto} - {formatNumber(item.quantidade)} litros
                </h2>
                {item.subprodutos && item.subprodutos.length > 0 && (
                  <ul className="list-disc pl-5 space-y-1 text-purple-700">
                    {item.subprodutos.map((sub, i) => (
                      <li key={i}>
                        <span className="font-medium">{sub.produto}</span>: {formatNumber(sub.quantidade)} litros
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}