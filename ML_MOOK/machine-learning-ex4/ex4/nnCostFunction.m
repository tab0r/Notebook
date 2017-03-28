function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m

X = [ones(m, 1) X];  % m by nn_params + 1

% handy dandy accumulators

partial_Sum = 0;

Delta_1 = zeros(hidden_layer_size, input_layer_size + 1);
Delta_2 = zeros(num_labels, hidden_layer_size + 1);

A1 = zeros(m, input_layer_size +1);
Z2 = zeros(m, hidden_layer_size);
A2 = zeros(m, hidden_layer_size +1);
Z3 = zeros(m, hidden_layer_size +1);
A3 = zeros(m, num_labels);

% convert y into binary matrix

y_Matrix = zeros(m, num_labels);

for i = 1:m
  for c = 1:num_labels
    if y(i) == c
      y_Matrix(i, c) = 1;
     endif
   endfor
endfor

for i = 1:m
  % feedforward to obtain outputs
  
  a1 = X(i, :)';
  z2 = Theta1 * a1;
  a2 = sigmoid(z2);
  a2 = [1; a2];
  z3 = Theta2 * a2;
  a3 = sigmoid(z3);
  
  inner_sum = 0;
  
  for k = 1:num_labels
    % calculate inner sum
    inner_sum = inner_sum + (-y_Matrix(i, k)*log(a3(k))-(1-y_Matrix(i, k))*log(1-a3(k)));
  endfor  
  
  partial_Sum = partial_Sum + inner_sum;
  
  % store loop variables in the accumulators for backpropagation
  
  A1(i, :) = a1;
  Z2(i, :) = z2';
  A2(i, :) = a2;
  %Z3(i, :) = z3;
  A3(i, :) = a3;
 
endfor

 % Part 2: Implement the backpropagation algorithm to compute the gradients
  %         Theta1_grad and Theta2_grad. You should return the partial derivatives of
  %         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
  %         Theta2_grad, respectively. After implementing Part 2, you can check
  %         that your implementation is correct by running checkNNGradients
  %
  %         Note: The vector y passed into the function is a vector of labels
  %               containing values from 1..K. You need to map this vector into a 
  %               binary vector of 1's and 0's to be used with the neural network
  %               cost function.
  %
  %         Hint: We recommend implementing backpropagation using a for-loop
  %               over the training examples if you are implementing it for the 
  %               first time.
  
  del_3 = A3 - y_Matrix;
  del_2 = Theta2(:,2:end)'*del_3';
  del_2 = del_2'.*sigmoidGradient(Z2);
  Delta_1 = del_2'*A1;
  Delta_2 = del_3'*A2;
  
Theta1_regTerm = (lambda/m).*Theta1;
Theta1_regTerm(:, 1) = 0;

Theta2_regTerm = (lambda/m).*Theta2;
Theta2_regTerm(:, 1) = 0;

Theta1_grad = (1/m).*Delta_1+Theta1_regTerm;
Theta2_grad = (1/m).*Delta_2+Theta2_regTerm;

% square theta matrices and drop zeroth terms
T1squares = Theta1.^2;
T1squares = T1squares(:,2:end);

T2squares = Theta2.^2;
T2squares = T2squares(:,2:end);

reg_term = (lambda/(2*m))*(sum(sum(T1squares))+sum(sum(T2squares)));

J = (1/m)*partial_Sum + reg_term;


% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%



















% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
