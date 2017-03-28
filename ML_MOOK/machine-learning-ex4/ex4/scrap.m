for i = 1:m
  inner_Sum = 0;
  for k = 1:num_labels
    yIK = y_Matrix(i, k);
    h = A3(k, i);
    inner_Sum = -yIK*log(h)-(1-yIK)*log(1-h);
  endfor
  partial_Sum = partial_Sum + inner_Sum;    
endfor

%super vectorized stuffs
%Z2 = Theta1 * X' ;   % hidden_layer_size by m
%A2 = sigmoid(Z2);    % "                    "
%A2 = [ones(1, m); A2];

%Z3 = Theta2 * A2;    % output_layer_size by m
%A3 = sigmoid(Z3);