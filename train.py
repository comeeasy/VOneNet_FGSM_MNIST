# %%

import torch
import torch.optim as optim
import torch.nn as nn
import torch.functional as F

import data
import ML_model
from tqdm import tqdm

def model_train():
    print('[INFO] train with origin data')

    # hyperparameter
    batch_size = 64
    learning_rate = 1e-3
    epochs = 5

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'train with {device}')

    # get data
    print('[INFO] getting data')
    train_data, label_data = data.get_mnist(batch_size)

    # get model (AlexNet)
    model = ML_model.MNIST_net(layers=3, num_classes=10)
    model.eval()
    model = model.to(device)

    optimizer = optim.Adam(params=model.parameters(), lr=learning_rate)
    costF = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        avg_cost = 0
        total_batch = len(train_data)

        for X, Y in tqdm(train_data):
            X = X.view(-1, 28 * 28).to(device)
            Y = Y.to(device)

            prediction = model(X)
            cost = costF(prediction, Y)

            optimizer.zero_grad()
            cost.backward()
            optimizer.step()

            avg_cost += cost / total_batch

        print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

    # save weights
<<<<<<< HEAD
    torch.save(model, 'weights/trained_Alexnet.pt')
=======
    torch.save(model, 'weights/trained_MNISTnet.pt')
>>>>>>> b844d971a4975c18dd51e60961d06f0a3319edc1

from adversarial_attack import generate_image_adversary
def fine_tune():
    print('[INFO] fine-tuning with adversarial images')

    # hyperparameter
    batch_size = 64
    learning_rate = 1e-4
<<<<<<< HEAD
    epochs = 5
=======
    epochs = 10
>>>>>>> b844d971a4975c18dd51e60961d06f0a3319edc1
    print(f'[INFO] hyperparameters : batch size:{batch_size}, lr:{learning_rate}, epochs:{epochs}')


    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'[INFO] train with {device}')

    # get data
    print('[INFO] getting data')
    train_data, _ = data.get_mnist(batch_size)

    # get model

    print('[INFO] getting model')
    model = torch.load(f='./weights/trained_MNISTnet.pt')
    model.eval()
    model = model.to(device)

    optimizer = optim.Adam(params=model.parameters(), lr=learning_rate)
    costF = nn.CrossEntropyLoss().to(device)

    for epoch in range(epochs):
        avg_cost = 0
        total_batch = len(train_data)

        for img_batch, target_batch in tqdm(train_data):
            # generate adversarial image batch
            adv_img_batch = generate_image_adversary(model=model, img_batch=img_batch, target_batch=target_batch)
            adv_target_batch = target_batch

            adv_img_batch = adv_img_batch.view(-1, 28 * 28).to(device)
            adv_target_batch = adv_target_batch.to(device)

            prediction = model(adv_img_batch)
            cost = costF(prediction, adv_target_batch)

            optimizer.zero_grad()
            cost.backward()
            optimizer.step()

            avg_cost += cost / total_batch

        print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

    # save weights
    print('[INFO] saving model')
<<<<<<< HEAD
    torch.save(model, 'weights/fine-tuned_trained_Alexnet.pt')
=======
    torch.save(model, 'weights/fine-tuned_trained_MNISTnet.pt')
>>>>>>> b844d971a4975c18dd51e60961d06f0a3319edc1

if __name__ == '__main__':

    model_train()
    fine_tune()
