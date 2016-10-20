error = 10.0^(-8)

function f(x)
  return x^3 + 3 * x - 1
end

function g(x)
  return x * log(x) - 1
end

function h(x)
  return x^2 - sin(x)
end

function i(x)
  return (1 + x - x^3)/4
end

function j(x)
  return exp(x) + x
end

function bissecao(fun, a, b, w)
  x = 0

  while abs(a - b) > w
    x = (a + b) / 2.0

    if (fun(x) * fun(a)) < 0
      b = x
    else
      a = x
    end
  end

  return x
end

function falsa_posicao(fun, a, b, w)
  erro_relativo = 1.0
  x = 0.0
  y = 0.0

  while erro_relativo > w
    x = ((a * abs(fun(b))) + (b * abs(fun(a)))) / ((abs(fun(b)) + (abs(fun(a)))))

    if (fun(x)) < 0.0
      a = x
    else
      b = x
    end

    erro_relativo = abs(y - x)/x

    y = x
  end

  return x
end

println("Bisseção ", bissecao(f, -5.0, 5.0, error))
println("Falsa Posição ", falsa_posicao(f, -5.0, 5.0, error))
println("Bisseção ", bissecao(g, 0.0001, 3.0, error))
println("Falsa Posição ", falsa_posicao(g, 0.0001, 3.0, error))
println("Bisseção ", bissecao(h, -1.0, 1.0, error))
println("Falsa Posição ", falsa_posicao(h, -1.0, 1.0, error))
println("Bisseção ", bissecao(i, -2.0, 2.0, error))
println("Falsa Posição ", falsa_posicao(i, -2.0, 2.0, error))
println("Bisseção ", bissecao(j, -1.0, 1.0, error))
println("Falsa Posição ", falsa_posicao(j, -1.0, 1.0, error))
